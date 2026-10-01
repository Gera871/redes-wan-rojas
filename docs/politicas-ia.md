# docs/politicas-ia.md — Ciberdefensa y uso de IA

1. **Cero secretos en el código.** Las credenciales, tokens y llaves SSH nunca se escriben directamente en `app.py`. Se gestionan mediante variables de entorno en `.env`, el cual está protegido por `.gitignore`.

2. **Con IA pública solo se usan datos de ejemplo.** Nunca se pegan IPs reales, credenciales, topologías sensibles ni capturas del sistema productivo.

3. **Validación de entradas.** Todo dato ingresado por el usuario (IPs, prefijos, hostnames, comandos) se valida antes de procesarse. La librería `ipaddress` rechaza formatos inválidos y lanza excepciones controladas.

4. **Advertencia de configuraciones inseguras.** La herramienta aplica el principio de mínimo privilegio: SSH obligatorio sobre Telnet, puertos administrativos cerrados, contraseñas enmascaradas.

5. **No se ejecuta nada que no se entienda.** Cada comando generado por IA se revisa y prueba primero en el laboratorio autorizado.

6. **Solo laboratorio autorizado.** Todo acceso SSH/Telnet se realiza exclusivamente sobre la infraestructura del laboratorio del curso (rack físico, GNS3 o Packet Tracer del docente).

7. **Métrica de calidad.** La confiabilidad de la herramienta se mide con pruebas automatizadas y se reporta como porcentaje en `docs/pruebas.md`.