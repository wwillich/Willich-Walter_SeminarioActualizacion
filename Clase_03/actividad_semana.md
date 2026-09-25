# Actividad de la semana — Clase 03

Explicación de las tres situaciones problema trabajadas en clase, tal como se entregó en el aula virtual.

## 1. README duplicado

Creamos el repositorio en GitHub con la opción "Add a README file" activada y, por separado, inicializamos un repositorio local con `git init` y un README propio. Al vincularlos y ejecutar `git push`, Git rechazó el envío: el remoto contenía un commit inexistente en el repositorio local, y ambas historias no compartían ningún punto de origen. Lo resolvimos con `git pull origin main --allow-unrelated-histories`, que permite unificar historias independientes. Como los dos README entraban en conflicto, conservamos una única versión, registramos el commit de fusión y recién entonces el `git push` se completó correctamente.

## 2. Carpeta sin ignorar

La carpeta `datos_prueba` se incluyó en un commit y se envió a GitHub sin estar declarada en el `.gitignore`. Agregarla después no alcanza, porque el `.gitignore` solo afecta a los archivos que Git todavía no tiene bajo seguimiento, y esta carpeta ya estaba versionada. La solución fue `git rm -r --cached datos_prueba`, que la quita del índice del repositorio sin eliminarla del disco local. Luego registramos el cambio con un commit, lo enviamos con `git push` y dejamos la carpeta declarada en el `.gitignore` para evitar que vuelva a incluirse.

## 3. Ramas master / main

La configuración local de Git tenía `master` como rama por defecto, mientras que GitHub utiliza `main`. Al ejecutar `git push -u origin master`, en el repositorio remoto se creó una rama `master` que no coincidía con la rama principal esperada. Lo resolvimos renombrando la rama local con `git branch -m master main`, enviando `main` al remoto y eliminando la rama `master` con `git push origin --delete master`. Para evitar que se repita, configuramos `git config --global init.defaultBranch main`.
