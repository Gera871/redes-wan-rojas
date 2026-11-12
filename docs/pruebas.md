# docs/pruebas.md — Reporte de pruebas y % de confianza

## Objetivo
Verificar que la herramienta Enterprise WAN Architect funciona correctamente en todos sus módulos y calcular el porcentaje de confianza del sistema para el Corte 3.

## Pruebas ejecutadas

| ID | Módulo | Descripción | Resultado |
|----|--------|-------------|-----------|
| P1 | M1 | Sincronización de estado global (M1 → M2/M3/M4/M5) | ✅ OK |
| P2 | M2 | Cálculo de subredes IPv4 con `ipaddress` (RFC 1918) | ✅ OK |
| P3 | M2 | Generación de enlaces WAN /30 sin desperdicio | ✅ OK |
| P4 | M2 | Asignación de bloques IPv6 /64 por piso | ✅ OK |
| P5 | M3 | Generación del diagrama topológico jerárquico con DOT | ✅ OK |
| P6 | M3 | Cálculo de gateways, broadcast y hosts útiles | ✅ OK |
| P7 | M4 | Configuración Cisco IOS válida | ✅ OK |
| P8 | M4 | Configuración Huawei VRP válida | ✅ OK |
| P9 | M4 | Configuración Fortinet FortiOS válida | ✅ OK |
| P10 | M4 | Configuración MikroTik RouterOS válida | ✅ OK |
| P11 | M5 | Conexión SSH con Paramiko (autenticación por llave) | ✅ OK |
| P12 | M5 | Conexión Serial vía cable de consola (PuTTY) | ✅ OK |
| P13 | M0 | Guardado y carga de proyectos en formato JSON | ✅ OK |
| P14 | M6 | Validación de entradas (IPs inválidas rechazadas) | ✅ OK |
| P15 | M6 | Protección de credenciales (uso de llaves en lugar de contraseñas) | ✅ OK |

## Resultado global
**Pruebas superadas: 15 / 15 = 100 % de confianza**

## Método
Cada prueba se ejecutó manualmente sobre el entorno local (`localhost:8501`). Se validó el subnetting con `ipaddress`, el despliegue de configuraciones vía SSH (Paramiko) y vía Consola Serial (pyserial), y la persistencia de datos en el Módulo 0.