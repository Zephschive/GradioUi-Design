import gradio as gr

CSS = """ 
.gr-container {
    display: flex;
    justify-content: center;
}
"""

with gr.Blocks(css=CSS) as UI:

    with gr.Row():
        with gr.Column():
            with gr.Row():
                gr.Button("🖼️ Generate")
                gr.Button("Edit")

            gr.Dropdown(label="Style", show_label=True, choices=["blah", "blah"])
            gr.Textbox(label="Prompt",max_lines=4)

            gr.Slider(minimum=0, maximum=10,  step=1, label="Settings", show_label=True)
            gr.Button("🌌 Dream")

        gr.Image()
        with gr.Column():
            gr.Textbox()

UI.launch()
