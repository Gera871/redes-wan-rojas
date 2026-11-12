# Seguridad de la Herramienta

- **Autenticación:** No se utilizan contraseñas planas. La conexión a equipos se hace vía SSH usando llaves privadas (.pem, .rsa, id_rsa).
- **Conexión por Consola:** Para equipos sin IP, se usa puerto serial, restringiendo el acceso al cable físico.
- **Sanitización:** Todas las IPs y prefijos son validados con la librería `ipaddress`. Si el usuario ingresa datos erróneos, la app los rechaza.
- **Protección de datos:** Los proyectos se guardan localmente en archivos JSON (sin datos sensibles de conexión). El archivo `.env` está en `.gitignore`.