# Herramienta de Redes WAN — Gerardo Esteban Rojas Manquillo (trabajo individual)
Materia: Interconexión de Redes WAN
Repositorio (público): https://github.com/Gera871/redes-wan-rojas

## Qué hace esta herramienta
Enterprise WAN Architect es una plataforma SaaS en Streamlit que diseña, calcula y documenta la infraestructura de red WAN de un edificio multi-piso (hasta 50 pisos), con cálculo matemático real de subredes IPv4/IPv6, topología jerárquica renderizada con Graphviz, generación de configuraciones CLI para 4 fabricantes y despliegue SSH real con Paramiko.

## Funciones
- Subnetting / IP Planning (IPv4/IPv6, público/privado) con la librería `ipaddress` (RFC real).
- Modelado topológico jerárquico (ISP → Router Borde → Router Core → Switch Core → Pisos → DMZ) renderizado con Graphviz DOT.
- Generación de configuraciones: Cisco (IOS), Huawei (VRP), Fortinet (FortiOS), MikroTik (RouterOS).
- Agente SSH real con Paramiko para despliegue sobre la infraestructura autorizada del laboratorio.
- Ciberdefensa integrada (validación de entradas, contraseñas enmascaradas, `.env` + `.gitignore`).

## Cómo ejecutarla
1. Clona el repo: `git clone https://github.com/Gera871/redes-wan-rojas.git`
2. Crea el entorno virtual: `python3 -m venv venv`
3. Actívalo: `source venv/bin/activate`
4. Instala dependencias: `pip install -r requirements.txt`
5. Corre la app: `streamlit run app.py`
6. Abre `http://localhost:8501`

## Pruebas y % de confianza (Corte 3)
- Pruebas superadas: 15 de 15 = 100% (ver `docs/pruebas.md`)

## Documentos
- docs/politicas-ia.md · docs/pruebas.md · docs/manual.md

## Capturas (evidencias)
docs/capturas/ (01-subnetting.png ... 10-app-final.png)

## Autoevaluación (marca Sí/No)
| Criterio                          | ¿Cumplido? | Evidencia            |
|-----------------------------------|------------|----------------------|
| Subnetting funciona               | Sí         | 01-subnetting.png    |
| Carga de topología                | Sí         | 02-topologia.png     |
| Config Cisco y Huawei             | Sí         | 03 / 04              |
| Config Fortinet y MikroTik (C3)   | Sí         | 06 / 07              |
| Ciberdefensa (politicas-ia.md)    | Sí         | 08-ciberdefensa.png  |
| Pruebas con % de confianza (C3)   | Sí         | docs/pruebas.md      |