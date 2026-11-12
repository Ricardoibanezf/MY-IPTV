# Mi IPTV — selección personalizada y actualización diaria

Esta versión busca **únicamente** los canales solicitados dentro del archivo público `https://iptv-org.github.io/iptv/index.m3u` de IPTV-org. No agrega señales de proveedores externos ni crea enlaces inexistentes.

## Canales solicitados

- **ESPN Sports:** todas las variantes cuyo nombre empiece con `ESPN` que estén publicadas en el M3U de IPTV-org. No se garantiza ESPN premium ni que sean accesibles.
- **ESPN Latinoamérica/México:** están contemplados dentro de la búsqueda general de ESPN; no hay una regla adicional ni se duplican.
- **América TV (Perú):** nombres América TV / América Televisión, identificador de canal `.pe`.
- **ATV (Perú):** ATV / Andina de Televisión, identificador `.pe`.
- **CBS Boston (EE. UU.):** CBS News Boston, CBS Boston y WBZ-TV si aparecen.

**Importante:** se registran búsquedas, no se promete la disponibilidad de ningún canal. El resultado de cada actualización aparece en `status.json`, con el número de coincidencias por nombre. Los canales pueden faltar o estar bloqueados geográficamente. Si el listado oficial no incluye una señal de ESPN, este proyecto **no** la añade desde otra fuente.

## Activación (GitHub Pages sin servidor propio)

1. El repositorio ya está creado: `Ricardoibanezf/MY-IPTV`, rama `main`.
2. Los archivos ya están en la raíz: `config.json`, `scripts/build.py` y `.github/workflows/update.yml`.
3. En **Settings → Pages → Build and deployment → Source** selecciona **GitHub Actions**.
4. En **Actions → Actualizar mi IPTV → Run workflow** inicia la primera publicación.
5. Cuando termine, abre `https://ricardoibanezf.github.io/MY-IPTV/playlist.m3u` para agregar el enlace a TiviMate o Televizo. Puedes revisar coincidencias en `https://ricardoibanezf.github.io/MY-IPTV/status.json`.

El archivo se regenera cada día mediante GitHub Actions (el cron puede demorarse ocasionalmente). Configura tu reproductor para refrescar la playlist regularmente. Puedes editar `config.json` para cambiar las selecciones.

## Límites y derechos

- Los enlaces son externos; el proyecto no almacena ni retransmite vídeos.
- Las playlists y la página son **públicas**, sin inicio de sesión.
- El catálogo cambia, puede haber enlaces rotos o geo-restricciones. **La reproducción no está garantizada.**
- Para vender acceso o redistribuir comercialmente necesitas comprobar los derechos de cada transmisión: la licencia del código de IPTV-org no equivale a permisos comerciales de los canales.
