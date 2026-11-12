# MY-IPTV

Playlist M3U personalizada, creada a partir de la lista pública de [IPTV-org](https://github.com/iptv-org/iptv). Selecciona los canales indicados en `config.json` y genera una playlist que se actualiza automáticamente con GitHub Actions.

## Canales incluidos

| Grupo | Canales que busca |
| --- | --- |
| **Deportes - ESPN** | Todas las variantes disponibles cuyo nombre comienza con ESPN, incluidas las de México y Latinoamérica. **Una sola regla, sin duplicarlas por país.** |
| **Perú** | América TV / América Televisión y ATV / Andina de Televisión (con identificador de Perú). |
| **Estados Unidos - Boston** | CBS Boston, CBS News Boston o WBZ-TV, si aparecen en IPTV-org. |

**Nota:** Son criterios de búsqueda, no una garantía de disponibilidad. En particular, los canales premium de ESPN pueden no tener una transmisión pública accesible. El proyecto **no** añade enlaces de fuentes ajenas a IPTV-org.

## Enlaces para usar

- **Playlist M3U:** https://ricardoibanezf.github.io/MY-IPTV/playlist.m3u
- **Reporte de coincidencias:** https://ricardoibanezf.github.io/MY-IPTV/status.json
- **Ejecuciones automáticas:** https://github.com/Ricardoibanezf/MY-IPTV/actions/workflows/update.yml

Para ver los canales en TiviMate o Televizo, agrega la primera URL como **playlist M3U remota**. No necesitas descargar el archivo en cada actualización. Configura el reproductor para actualizar la playlist periódicamente.

## Cómo se actualiza

1. El flujo `.github/workflows/update.yml` se ejecuta **cada día a las 07:17 UTC** (la ejecución programada puede demorarse).
2. También se ejecuta cuando cambia `config.json`, `scripts/build.py` o el propio workflow.
3. El script `scripts/build.py` descarga el M3U oficial de IPTV-org y busca las coincidencias definidas en `config.json`.
4. Crea `playlist.m3u` y `status.json`, y los publica mediante **GitHub Pages**.

También puedes iniciar una actualización manual desde **Actions → Actualizar mi IPTV → Run workflow**.

La playlist pública solo cambia cuando se publica una nueva versión y el reproductor vuelve a cargarla. Si una señal desaparece del origen, no se recupera automáticamente de otra fuente.

## Cambiar canales

Edita el archivo [config.json](./config.json). Cada elemento dentro de `favorites` contiene un nombre descriptivo (`label`), patrones de coincidencia (`patterns`) y un grupo (`group`); las reglas de Perú incluyen el filtro `countries`.

Guarda el cambio en la rama `main` y GitHub Actions intentará generar de nuevo la playlist. El generador evita duplicar una misma entrada aunque coincida con varias reglas.

## Archivos del proyecto

- `config.json`: selección de canales.
- `scripts/build.py`: generador de la playlist y reporte.
- `.github/workflows/update.yml`: actualización y publicación en GitHub Pages.

## Limitaciones y derechos

- IPTV-org lista enlaces públicos de terceros; esta herramienta no aloja ni retransmite video.
- El acceso al repositorio y a la playlist publicada es **público**, sin nombres de usuario ni contraseñas.
- Algunos enlaces pueden fallar, estar sujetos a restricciones geográficas o desaparecer. Una coincidencia en `status.json` no confirma reproducción.
- La licencia del código de IPTV-org no concede automáticamente derechos comerciales sobre los canales. Antes de vender acceso, es necesario verificar las autorizaciones correspondientes.
