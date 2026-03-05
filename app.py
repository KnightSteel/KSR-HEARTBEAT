import gradio as gr
from harvester import harvest_video
from loguru import logger

# Configuración de Tema: Blindaje de Estilo KnightSteel
# Usamos las variables estándar para evitar el TypeError
theme = gr.themes.Soft(
    primary_hue="yellow",
    secondary_hue="gray",
    neutral_hue="slate",
).set(
    body_background_fill="#0a0a0a",
    block_background_fill="#111111",
    block_border_width="2px",
    button_primary_background_fill="#d4af37",
    button_primary_text_color="#000000",
)


def run_harvest(url):
    if not url:
        return "⚠️ Error: El Caballero requiere un link válido."
    try:
        # Llamamos al motor que ya probamos
        harvest_video(url)
        return f"✅ Cosecha completada. El video está en assets/videos."
    except Exception as e:
        logger.error(f"Fallo en la interfaz: {e}")
        return f"❌ Error en la matriz: {str(e)}"


with gr.Blocks(theme=theme, title="🛡️ KSR-HEARTBEAT") as demo:
    gr.Markdown(
        """
        # 🛡️ KSR-HEARTBEAT
        ### **Motor de Resonancia Vocal | The Foundry**
        ---
        """
    )

    with gr.Row():
        with gr.Column(scale=2):
            url_input = gr.Textbox(
                label="🔗 Enlace del Tesoro",
                placeholder="Pega aquí el link de YouTube...",
                lines=1,
            )
            harvest_btn = gr.Button("🚀 INICIAR COSECHA", variant="primary")

        with gr.Column(scale=1):
            output_log = gr.Textbox(label="📡 Estatus del Sistema", interactive=False)

    harvest_btn.click(fn=run_harvest, inputs=url_input, outputs=output_log)

    gr.Markdown(
        """
        <div style="text-align: center; color: #555; font-size: 0.8em; margin-top: 50px;">
            Forjado por KnightSteel | danweek@outlook.com | AURA & GENESIS Sync
        </div>
        """
    )

if __name__ == "__main__":
    # Lanzamos en el puerto 9999
    # inline=False para que no intente abrirse dentro de la terminal
    demo.launch(server_name="0.0.0.0", server_port=9999)
