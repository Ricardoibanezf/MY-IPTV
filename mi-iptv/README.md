# Mi IPTV — selección personalizada y actualización diaria

Esta versión busca **únicamente** los canales solicitados dentro del archivo público `https://iptv-org.github.io/iptv/index.m3u` de IPTV-org. No agrega señales de proveedores externos ni crea enlaces inexistentes.

## Canales solicitados

- **ESPN Sports:** todas las variantes cuyo nombre empiece con `ESPN` que estén publicadas en el M3U de IPTV-org. No se garantiza ESPN premium ni que sean accesibles.
- **ESPN Latinoamérica/México:** se incluyen cuando aparezcan. Ya están contemplados en la búsqueda de todos los ESPN; no se duplican.
- **América TV (Perú):** nombres América TV / América Televisión, identificador de canal `.pe`.
- **ATV (Perú):** ATV / Andina de Televisión, identificador `.pe`.
- **CBS Boston (EE. UU.):** CBS News Boston, CBS Boston y WBZ-TV si aparecen.

**Importante:** se registran búsquedas, no se promete la disponibilidad de ningún canal. El resultado de cada actualización aparece en `status.json`, con el número de coincidencias por nombre. Los canales pueden faltar o estar bloqueados geográficamente. Si el listado oficial no incluye una señal de ESPN, este proyecto **no** la añade desde otra fuente.

## Activación (GitHub Pages sin servidor propio)

1. Crea un repositorio **público** `mi-iptv` en GitHub, con la rama `main`.
2. Sube *el contenido* de esta carpeta con su estructura, incluido `.github/workflows/update.yml`. El ZIP está pensado para descargarse/descomprimirse; GitHub no ejecuta un ZIP subido como un solo archivo.
3. En **Settings → Pages → Build and deployment → Source** selecciona **GitHub Actions**.
4. En **Actions → Actualizar mi IPTV → Run workflow** inicia la primera publicación.
5. Cuando termine, abre `https://TU-USUARIO.github.io/mi-iptv/playlist.m3u` para agregar el enlace a TiviMate o Televizo. Puedes revisar coincidencias en `https://TU-USUARIO.github.io/mi-iptv/status.json`.

El archivo se regenera cada día mediante GitHub Actions (el cron puede demorarse ocasionalmente). Configura tu reproductor para refrescar la playlist regularmente. Puedes editar `config.json` para cambiar las selecciones.

## Límites y derechos

- Los enlaces son externos; el proyecto no almacena ni retransmite vídeos.
- Las playlists y la página son **públicas**, sin inicio de sesión.
- El catálogo cambia, puede haber enlaces rotos o geo-restricciones. **La reproducción no está garantizada.**
- Para vender acceso o redistribuir comercialmente necesitas comprobar los derechos de cada transmisión: la licencia del código de IPTV-org no equivale a permisos comerciales de los canales.
