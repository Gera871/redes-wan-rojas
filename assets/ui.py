"""
Enterprise WAN Architect — Componentes UI reutilizables.
Todos los helpers devuelven HTML listo para st.markdown(..., unsafe_allow_html=True)
o lo inyectan directamente. NO contienen lógica de negocio.
"""
import os
import streamlit as st


# ---------- Iconos SVG (Lucide) embebidos, sin dependencias ----------
ICONS = {
    "globe": '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>',
    "settings": '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 1 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 1 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 1 1-2.83-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 1 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 1 1 2.83-2.83l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 1 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 1 1 2.83 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 1 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>',
    "chart": '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>',
    "network": '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="2" width="6" height="6" rx="1"/><rect x="2" y="16" width="6" height="6" rx="1"/><rect x="16" y="16" width="6" height="6" rx="1"/><path d="M12 8v4M5 16v-2h14v2"/></svg>',
    "terminal": '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>',
    "shield": '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "download": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>',
    "play": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="5 3 19 12 5 21 5 3"/></svg>',
    "save": '<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"/><polyline points="17 21 17 13 7 13 7 21"/><polyline points="7 3 7 8 15 8"/></svg>',
    "check": '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>',
    "cpu": '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="4" width="16" height="16" rx="2"/><rect x="9" y="9" width="6" height="6"/><line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/><line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/><line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/><line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/></svg>',
    "sparkles": '<svg xmlns="http://www.w3.org/2000/svg" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v18M3 12h18M5.6 5.6l12.8 12.8M18.4 5.6L5.6 18.4"/></svg>',
    "building": '<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="9" y1="6" x2="9" y2="6.01"/><line x1="15" y1="6" x2="15" y2="6.01"/><line x1="9" y1="10" x2="9" y2="10.01"/><line x1="15" y1="10" x2="15" y2="10.01"/><line x1="9" y1="14" x2="9" y2="14.01"/><line x1="15" y1="14" x2="15" y2="14.01"/><path d="M9 22v-4h6v4"/></svg>',
}


def icon(name: str, size: int = 18) -> str:
    """Devuelve el SVG del icono con tamaño opcional."""
    svg = ICONS.get(name, "")
    if not svg:
        return ""
    if size != 18:
        svg = svg.replace('width="18"', f'width="{size}"').replace('height="18"', f'height="{size}"')
    return svg


def inject_css():
    """Inyecta el CSS global en la app."""
    css_path = os.path.join(os.path.dirname(__file__), "styles.css")
    if os.path.exists(css_path):
        with open(css_path, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def hero(title: str, subtitle: str, badge: str = None, icon_name: str = "globe"):
    """Header tipo Hero con gradiente y badge opcional."""
    badge_html = (
        f'<div class="wan-hero-badge">{icon("sparkles", 12)} {badge}</div>'
        if badge else ""
    )
    html = f"""
    <div class="wan-hero">
        {badge_html}
        <h1 class="wan-hero-title">{icon(icon_name, 26)} {title}</h1>
        <p class="wan-hero-sub">{subtitle}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def section(title: str, subtitle: str = None, icon_name: str = "settings"):
    """Título de sección con icono."""
    sub = f'<p class="wan-section-sub">{subtitle}</p>' if subtitle else ""
    html = f"""
    <div class="wan-section">
        <div class="wan-section-icon">{icon(icon_name, 18)}</div>
        <div>
            <h3 class="wan-section-title">{title}</h3>
            {sub}
        </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def mac_terminal(title: str, content: str):
    """Ventana flotante estilo terminal macOS."""
    html = f"""
    <div class="mac-window">
        <div class="mac-header">
            <span class="mac-dot-red"></span>
            <span class="mac-dot-yellow"></span>
            <span class="mac-dot-green"></span>
            <span class="mac-title">{title}</span>
        </div>
        <pre class="mac-body">{content}</pre>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def metric(label: str, value: str, delta: str = None):
    """Tarjeta de métrica."""
    delta_html = f'<div class="wan-metric-delta">{delta}</div>' if delta else ""
    html = f"""
    <div class="wan-metric">
        <div class="wan-metric-label">{label}</div>
        <div class="wan-metric-value">{value}</div>
        {delta_html}
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def badge(text: str, status: str = "info") -> str:
    """Devuelve HTML de un badge (no lo renderiza, para incrustar)."""
    return f'<span class="wan-badge wan-badge-{status}">{icon("check", 12)} {text}</span>'


def device(name: str, dev_type: str, ip: str, status: str = "online"):
    """Tarjeta de dispositivo de red."""
    status_map = {
        "online": ("success", "En Línea"),
        "offline": ("error", "Desconectado"),
        "warning": ("warning", "Alerta"),
    }
    st_key, label = status_map.get(status, ("info", status))
    html = f"""
    <div class="wan-device">
        <div>
            <p class="wan-device-name">{name}</p>
            <p class="wan-device-meta">{dev_type} &bull; {ip}</p>
        </div>
        <div>{badge(label, st_key)}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)


def progress(value: float, max_value: float = 100.0, label: str = "Progreso"):
    """Barra de progreso estilizada."""
    pct = min(max((value / max_value) * 100, 0), 100) if max_value else 0
    html = f"""
    <div class="wan-progress">
        <div class="wan-progress-fill" style="width: {pct}%;"></div>
    </div>
    <div class="wan-progress-meta">
        <span>{label}</span>
        <span>{pct:.1f}%</span>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)