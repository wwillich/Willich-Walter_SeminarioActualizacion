# Clase 03 — GitHub, Codespaces y control de versiones

## Objetivo

En esta clase vinculamos el repositorio local con GitHub (`remote`, `origin`, ramas `main`/`master`), trabajamos con GitHub Codespaces y analizamos tres situaciones problema frecuentes al combinar Git con un repositorio remoto:

1. **README duplicado:** el repositorio remoto y el local se inician con historias independientes.
2. **Carpeta sin ignorar:** se versiona contenido que no correspondía y el `.gitignore` se agrega después.
3. **Ramas master / main:** la rama principal local y la remota tienen nombres distintos.

La entrega de la semana consiste en explicar qué ocurrió en cada situación y cómo se resolvió.

## Contenido de la carpeta

| Archivo | Descripción |
|---|---|
| `actividad_semana.md` | Explicación de las tres situaciones (entrega del aula virtual) |
| `reproducir_situaciones.ps1` | Script que reproduce las tres situaciones de principio a fin, con el error y su solución |
| `README.md` | Este archivo |

## Requisitos

- Git 2.28 o superior (necesario para la opción `-b` de `git init`)
- Windows con PowerShell

El script no requiere una cuenta de GitHub: cada repositorio remoto se simula con un repositorio *bare* en una carpeta temporal, que cumple el mismo rol que GitHub.

## Cómo reproducirlo

Desde la carpeta `Clase_03`:

```powershell
# Las tres situaciones en secuencia
powershell -ExecutionPolicy Bypass -File .\reproducir_situaciones.ps1

# Una situación puntual
powershell -ExecutionPolicy Bypass -File .\reproducir_situaciones.ps1 -Situacion 2
```

Los repositorios de prueba se generan en `%TEMP%\clase03_situaciones` y se eliminan en cada nueva ejecución. El script no modifica la configuración global de Git.

### Comandos clave de cada situación

```powershell
# 1. README duplicado
git pull origin main --allow-unrelated-histories
# resolver el conflicto en README.md, luego add + commit
git push

# 2. Carpeta sin ignorar
git rm -r --cached datos_prueba
git commit -m "Deja de versionar datos_prueba"
git push
# y declarar datos_prueba/ en el .gitignore

# 3. Ramas master / main
git branch -m master main
git push -u origin main
git push origin --delete master
git config --global init.defaultBranch main
```

> **Nota:** en GitHub, si `master` quedó configurada como rama por defecto del repositorio, primero hay que cambiarla a `main` desde *Settings → Branches*. De lo contrario, GitHub no permite eliminarla.

## Resultado esperado

- **Situación 1:** primero aparece `! [rejected] main -> main (fetch first)`, luego `fatal: refusing to merge unrelated histories` y, al usar la opción `--allow-unrelated-histories`, un conflicto en `README.md`. Una vez resuelto, el `git push` se completa y `git log --graph` muestra ambas historias unificadas en un commit de fusión.
- **Situación 2:** con la carpeta ya declarada en el `.gitignore`, `git status` sigue mostrando `datos_prueba/datos.csv` como modificado. Después de `git rm --cached`, el archivo desaparece del repositorio remoto pero **se conserva en el disco local**.
- **Situación 3:** el repositorio remoto comienza con una única rama `refs/heads/master` y termina con una única rama `refs/heads/main`, con la rama local `main` vinculada a `origin/main`.
