import yt_dlp
import os
from loguru import logger

# --- CONFIGURACIÓN DE RUTAS DE ALTA JERARQUÍA ---
# Detectamos la ubicación real del script para que funcione en AURA y GENESIS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
VIDEO_DIR = os.path.join(BASE_DIR, "assets", "videos")


def harvest_video(url):
    """
    Descarga video en máxima fidelidad (4K/1080p) para procesamiento de IA.
    """
    # Verificamos que el santuario de archivos exista
    if not os.path.exists(VIDEO_DIR):
        os.makedirs(VIDEO_DIR, exist_ok=True)
        logger.info(f"📁 Creando almacén de activos en: {VIDEO_DIR}")

    ydl_opts = {
        # Buscamos la mejor calidad de video (mp4) y audio (m4a)
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "outtmpl": os.path.join(VIDEO_DIR, "%(title)s.%(ext)s"),
        "noplaylist": True,
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",
            }
        ],
        "quiet": False,
        "no_warnings": False,
    }

    try:
        logger.info(f"🚀 Iniciando recolección de luz: {url}")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        logger.success(
            "✅ Cosecha completada. El material está listo para el despertar."
        )
    except Exception as e:
        logger.error(f"❌ Error en la frecuencia de descarga: {e}")


if __name__ == "__main__":
    print("\n" + "=" * 40)
    print("🛡️  KSR-HEARTBEAT | VIDEO HARVESTER  🛡️")
    print("=" * 40)
    link = input("🔗 Pega el link del Tesoro (YouTube/Vimeo): ")
    if link.strip():
        harvest_video(link)
    else:
        logger.warning("⚠️ No pusiste ningún link, carnal. Abortando misión.")
