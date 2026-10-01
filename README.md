# Herramienta de Redes WAN — Gerardo Esteban Rojas Manquillo
Materia: Interconexión de Redes WAN
Repositorio (público): https://github.com/Gera871/redes-wan-rojas

## Qué hace esta herramienta
Enterprise WAN Architect es una plataforma SaaS en Streamlit que diseña, calcula y despliega infraestructura de red WAN para edificios multi-piso con subnetting real (ipaddress), topología jerárquica (Graphviz DOT), configuraciones CLI para 4 fabricantes y despliegue SSH con Paramiko.

## Funciones
- Subnetting / IP Planning (IPv4/IPv6, público/privado)
- Carga de la topología (dispositivos, enlaces, ISP)
- Generación de configuraciones: Cisco, Huawei, Fortinet, MikroTik
- Ciberdefensa contra IA (aplica docs/politicas-ia.md)

## Cómo ejecutarla
1. Clona el repo: `git clone https://github.com/Gera871/redes-wan-rojas.git`
2. Crea el venv: `python3 -m venv venv`
3. Actívalo: `source venv/bin/activate`
4. Instala: `pip install -r requirements.txt`
5. Corre: `streamlit run app.py`

## Pruebas y % de confianza
- Pruebas superadas: 15 de 15 = 100% (ver docs/pruebas.md)

## Documentos
- docs/politicas-ia.md · docs/pruebas.md · docs/manual.md · docs/informe-corte2.pdf

## Capturas (evidencias)
- 01-subnetting.png
- 02-topologia.png
- 03-config-cisco.png
- 04-config-huawei.png
- 05-github-commits.png

## Autoevaluación
| Criterio                          | ¿Cumplido? | Evidencia            |
|-----------------------------------|------------|----------------------|
| Subnetting funciona               | Sí         | 01-subnetting.png    |
| Carga de topología                | Sí         | 02-topologia.png     |
| Config Cisco y Huawei             | Sí         | 03 / 04              |
| Ciberdefensa (politicas-ia.md)    | Sí         | 08-ciberdefensa.png  |
| Pruebas con % de confianza        | Sí         | docs/pruebas.md      |