# Actividad de la semana — Clase 03

Explicación de las 3 situaciones problema, tal como la subí al aula virtual.

## 1. README duplicado

Creé el repo en GitHub con el README tildado y, por otro lado, armé un repo local con `git init` y su propio README. Al conectarlos y hacer `git push`, Git lo rechazó: el remoto ya tenía un commit que yo no tenía, y las dos historias no tenían nada en común. Lo resolví con `git pull origin main --allow-unrelated-histories`, que une las dos historias. Como los dos README chocaban, me quedé con una sola versión, hice el commit y recién ahí pude pushear.

## 2. Carpeta sin ignorar

Subí la carpeta `datos_prueba` sin tenerla en el `.gitignore`. Agregarla después no alcanza, porque el `.gitignore` solo afecta a los archivos que Git todavía no sigue, y esta carpeta ya estaba trackeada. La solución fue `git rm -r --cached datos_prueba`, que la saca del repo pero no la borra de mi compu. Después hice commit, push y dejé la carpeta en el `.gitignore` para que no se vuelva a subir.

## 3. Ramas master / main

Mi Git local tenía configurado `master` como rama por defecto, y GitHub usa `main`. Al hacer `git push -u origin master`, en GitHub apareció una rama `master` que no coincidía con la principal que esperaba. Lo resolví renombrando la rama local con `git branch -m master main`, subiendo `main` y borrando `master` del remoto con `git push origin --delete master`. Para que no vuelva a pasar, dejé `git config --global init.defaultBranch main`.
