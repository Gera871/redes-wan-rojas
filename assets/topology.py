"""
Enterprise WAN Architect — Generador de Topología Jerárquica Real.
Calcula subredes con `ipaddress` (RFC) y genera un string DOT
que st.graphviz_chart() renderiza en el navegador sin dependencias del sistema.
"""
import ipaddress


def _split_subnets(base_network, count, new_prefix):
    try:
        return list(base_network.subnets(new_prefix=new_prefix))[:count]
    except ValueError:
        return []


def _host_or_empty(subnet, index):
    hosts = list(subnet.hosts())
    if 0 <= index < len(hosts):
        return str(hosts[index])
    return "N/A"


def build_topology_dot(cfg: dict) -> tuple:
    """Genera (dot_string, detalle) calculados 100% con ipaddress."""
    base_network = ipaddress.ip_network(
        f"{cfg['red_base']}/{cfg['prefijo']}", strict=False
    )

    wan_links = _split_subnets(base_network, count=6, new_prefix=30)
    num_pisos = int(cfg["pisos"])
    lan_subnets = _split_subnets(base_network, count=num_pisos + 1, new_prefix=26)
    dmz_subnet = lan_subnets[-1] if lan_subnets else None

    C_ROUTER, C_SWITCH, C_HOST = "#1b2637", "#151e2c", "#111927"
    C_ISP, C_DMZ = "#2b1f0f", "#1e2b1e"
    BORDER, BORDER_D = "#3cc7b7", "#54c98a"

    L = []
    L.append('digraph WAN_Topology {')
    L.append('  rankdir=TB; bgcolor="#0d1420"; fontname="Helvetica";')
    L.append('  fontcolor="#e7edf6";')
    L.append(f'  label="Topología Calculada — {cfg["nombre"]} ({num_pisos} pisos)";')
    L.append('  labelloc="t"; fontsize=16; nodesep=0.5; ranksep=0.7;')
    L.append('  node [fontname="Helvetica", fontsize=10, fontcolor="#e7edf6", style="filled,rounded", shape=box, penwidth=2];')
    L.append('  edge [fontname="Helvetica", fontsize=9, fontcolor="#a7b4c8", color="#3cc7b7", penwidth=2];')

    L.append(f'  ISP [label="ISP Cloud\\n209.165.200.224/29", shape=ellipse, fillcolor="{C_ISP}", color="#e0a44f"];')

    wan_isp_ip = _host_or_empty(wan_links[0], 0) if len(wan_links) > 0 else "N/A"
    wan_core_ip = _host_or_empty(wan_links[0], 1) if len(wan_links) > 0 else "N/A"
    L.append(f'  R_EDGE [label="Router Borde (2911)\\nWAN: {wan_core_ip}/30", fillcolor="{C_ROUTER}", color="{BORDER}"];')

    wan1_r2_ip = _host_or_empty(wan_links[1], 1) if len(wan_links) > 1 else "N/A"
    L.append(f'  R_CORE [label="Router Core (2911)\\nWAN: {wan1_r2_ip}/30", fillcolor="{C_ROUTER}", color="{BORDER}"];')

    L.append(f'  SW_CORE [label="Switch Core (2960)\\nVLANs Troncales", fillcolor="{C_SWITCH}", color="{BORDER}"];')

    if dmz_subnet is not None:
        dmz_ip = _host_or_empty(dmz_subnet, 0)
        L.append(f'  SRV_DMZ [label="Servidor DMZ\\n{dmz_ip}/{dmz_subnet.prefixlen}", shape=cylinder, fillcolor="{C_DMZ}", color="{BORDER_D}"];')

    L.append(f'  HOSTS [label="Hosts / Usuarios\\n{cfg["clientes"]} clientes", shape=note, fillcolor="{C_HOST}", color="#6d7c95"];')

    L.append('  subgraph cluster_pisos {')
    L.append(f'    label="Pisos del Edificio ({num_pisos})";')
    L.append('    bgcolor="#0f1826"; color="#28344a"; fontcolor="#a7b4c8"; style=rounded;')
    for i in range(num_pisos):
        if i < len(lan_subnets) - 1:
            sn = lan_subnets[i]
            gw = _host_or_empty(sn, 0)
            vlan_id = 10 + (i * 10)
            L.append(f'    SW_P{i+1} [label="Piso {i+1}\\nVLAN {vlan_id}\\nGW: {gw}/{sn.prefixlen}", fillcolor="{C_SWITCH}", color="{BORDER}"];')
    L.append('  }')

    L.append(f'  ISP -> R_EDGE [label="{wan_isp_ip} - {wan_core_ip}"];')
    wan_link_label = str(wan_links[1]) if len(wan_links) > 1 else "N/A"
    L.append(f'  R_EDGE -> R_CORE [label="WAN {wan_link_label}"];')
    L.append('  R_CORE -> SW_CORE [label="Trunk 802.1Q"];')
    if dmz_subnet is not None:
        L.append('  SW_CORE -> SRV_DMZ [label="VLAN DMZ"];')
    for i in range(num_pisos):
        if i < len(lan_subnets) - 1:
            L.append(f'  SW_CORE -> SW_P{i+1} [style=dashed];')
    L.append('  SW_CORE -> HOSTS [label="Acceso LAN", style=dotted];')
    L.append('}')

    dot_string = "\n".join(L)

    detalle = {
        "wan_links": [
            {"Segmento": f"WAN {i+1}", "Subred /30": str(sn),
             "IP A (host 1)": _host_or_empty(sn, 0), "IP B (host 2)": _host_or_empty(sn, 1)}
            for i, sn in enumerate(wan_links[:3])
        ],
        "lan_pisos": [
            {"Piso": f"Piso {i+1}" if i < num_pisos else "DMZ",
             "VLAN": 10 + (i * 10), "Subred": str(sn.network_address),
             "Prefijo": f"/{sn.prefixlen}", "Gateway": _host_or_empty(sn, 0),
             "Broadcast": str(sn.broadcast_address),
             "Hosts útiles": len(list(sn.hosts()))}
            for i, sn in enumerate(lan_subnets[:num_pisos])
        ],
        "dmz": {
            "Subred": str(dmz_subnet.network_address) if dmz_subnet else "N/A",
            "Prefijo": f"/{dmz_subnet.prefixlen}" if dmz_subnet else "N/A",
            "Servidor": _host_or_empty(dmz_subnet, 0) if dmz_subnet else "N/A",
        },
    }
    return dot_string, detalle