# Bitácora de errores — TP Integrador

Registro de los errores que aparecieron durante el trabajo, en orden cronológico. Cada entrada incluye el mensaje completo, dónde apareció, qué lo causaba y cómo se resolvió.

## Error 1 — Git Bash no arranca por un error de `fork`

- **Cuándo:** 13/10/2026 20:30 · **Fase:** 1
- **Dónde apareció:** mi compu
- **Qué estaba haciendo:** crear la carpeta `TP_Integrador/` y sus archivos iniciales con un único comando en Git Bash.
- **Mensaje completo:**
  ```
  Exit code 254
        0 [main] bash 1691 dofork: child -1 - forked process 17364 died unexpectedly, retry 0, exit code 0xC0000142, errno 11
  /etc/profile: fork: retry: Resource temporarily unavailable
  1400720 [main] bash 1691 dofork: child -1 - forked process 17372 died unexpectedly, retry 0, exit code 0xC0000142, errno 11
  /etc/profile: fork: retry: Resource temporarily unavailable
  3619217 [main] bash 1691 dofork: child -1 - forked process 14508 died unexpectedly, retry 0, exit code 0xC0000142, errno 11
  /etc/profile: fork: retry: Resource temporarily unavailable
  7835796 [main] bash 1691 dofork: child -1 - forked process 7636 died unexpectedly, retry 0, exit code 0xC0000142, errno 11
  /etc/profile: fork: retry: Resource temporarily unavailable
  16096389 [main] bash 1691 dofork: child -1 - forked process 10840 died unexpectedly, retry 0, exit code 0xC0000142, errno 11
  /etc/profile: fork: Resource temporarily unavailable
  ```
- **Qué lo causaba:** Git Bash no pudo crear procesos hijos al iniciar `/etc/profile`. El código `0xC0000142` indica que un proceso de Windows no pudo inicializarse, y `errno 11` (`Resource temporarily unavailable`) apunta a falta de recursos del sistema en ese momento. No se confirmó cuál fue el recurso agotado.
- **Cómo lo resolví, paso a paso:**
  1. Verifiqué con `Test-Path TP_Integrador` y `git status --short` que el comando no había creado nada.
  2. Pasé a PowerShell, que no depende de `fork`.
  3. Creé los archivos uno por uno y el entorno virtual con `python -m venv .venv`, sin errores.
- **Qué aprendí:** conviene comprobar qué alcanzó a ejecutarse antes de repetir un comando que falló a la mitad, y tener un segundo intérprete a mano. En Windows, PowerShell evita este problema porque no usa `fork`.
