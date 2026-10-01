# docs/pruebas.md — Reporte de pruebas y % de confianza

## Objetivo
Verificar que la herramienta Enterprise WAN Architect funciona correctamente en todos sus módulos y calcular el porcentaje de confianza del sistema.

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
| P11 | M5 | Conexión SSH con Paramiko (manejo de excepciones) | ✅ OK |
| P12 | M5 | Terminal estilo macOS renderizada correctamente | ✅ OK |
| P13 | M6 | Validación de entradas (IPs inválidas rechazadas) | ✅ OK |
| P14 | M6 | Contraseñas enmascaradas con `type="password"` | ✅ OK |
| P15 | M6 | Sin credenciales hardcodeadas en el código | ✅ OK |

## Resultado global
**Pruebas superadas: 15 / 15 = 100 % de confianza**

## Método
Cada prueba se ejecutó manualmente en el navegador sobre el entorno local (`localhost:8501`) con la red base `192.168.0.0/22` y un escenario de 15 pisos. Los resultados se verificaron contra los cálculos de `ipaddress` y la sintaxis oficial de cada fabricante.