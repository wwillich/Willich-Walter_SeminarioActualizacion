# Clase 03 — GitHub, Codespaces y control de versiones

## Objetivo

En esta clase conecté el repo local con GitHub (`remote`, `origin`, `main`/`master`), probé Codespaces y trabajé tres situaciones problema que suelen aparecer al usar Git con GitHub:

1. **README duplicado:** el repo remoto y el local arrancan con historias distintas.
2. **Carpeta sin ignorar:** subí algo que no correspondía y el `.gitignore` llegó tarde.
3. **Ramas master / main:** la rama local y la del remoto no se llaman igual.

La entrega de la semana es explicar con mis palabras qué pasó en cada una y cómo lo resolví.

## Contenido de la carpeta

| Archivo | Qué tiene |
|---|---|
| `actividad_semana.md` | Mi explicación de las 3 situaciones (lo que entregué en el aula virtual) |
| `reproducir_situaciones.ps1` | Script que reproduce las 3 situaciones de punta a punta, con el error y la solución |
| `README.md` | Este archivo |

## Requisitos

- Git 2.28 o superior (por la opción `-b` de `git init`)
- Windows con PowerShell

No hace falta cuenta de GitHub para correr el script: cada "remoto" es un repo *bare* en una carpeta temporal que cumple el mismo papel que GitHub.

## Cómo reproducirlo

Parado en la carpeta `Clase_03`:

```powershell
# Las 3 situaciones seguidas
powershell -ExecutionPolicy Bypass -File .\reproducir_situaciones.ps1

# O una sola
powershell -ExecutionPolicy Bypass -File .\reproducir_situaciones.ps1 -Situacion 2
```

Los repos de prueba quedan en `%TEMP%\clase03_situaciones` y se borran cada vez que corrés el script de nuevo. No toca tu configuración global de Git.

### Comandos clave de cada situación

```powershell
# 1. README duplicado
git pull origin main --allow-unrelated-histories
# resolver el conflicto en README.md, add + commit
git push

# 2. Carpeta sin ignorar
git rm -r --cached datos_prueba
git commit -m "Deja de trackear datos_prueba"
git push
# y agregar datos_prueba/ al .gitignore

# 3. Ramas master / main
git branch -m master main
git push -u origin main
git push origin --delete master
git config --global init.defaultBranch main
```

> En GitHub real, si `master` quedó como rama por defecto del repo, primero hay que cambiarla a `main` en *Settings → Branches*. Si no, GitHub no deja borrarla.

## Resultado esperado

- **Situación 1:** primero aparece `! [rejected] main -> main (fetch first)`, después `fatal: refusing to merge unrelated histories` y por último un conflicto en `README.md`. Una vez resuelto, el push pasa y `git log --graph` muestra las dos historias unidas en un merge.
- **Situación 2:** después de agregar la carpeta al `.gitignore`, `git status` sigue mostrando `datos_prueba/datos.csv` como modificado. Con `git rm --cached` desaparece del remoto, pero el archivo sigue en el disco.
- **Situación 3:** el remoto primero tiene solo `refs/heads/master`. Al final tiene solo `refs/heads/main`, y la rama local `main` queda asociada a `origin/main`.
