import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"
    page.window_width = 400
    page.window_height = 500
    page.padding = 20

    nome = ft.TextField(
        label="Nome",
        width=350
    )

    email = ft.TextField(
        label="Email",
        width=350
    )

    mensagem = ft.TextField(
        label="Mensagem",
        multiline=True,
        min_lines=4,
        max_lines=6,
        width=350
    )

    resultado = ft.Text(
        value="",
        size=16
    )

    def enviar_formulario(e):
        if nome.value and email.value and mensagem.value:
            resultado.value = f"Formulário enviado com sucesso! Obrigado, {nome.value}."

            nome.value = ""
            email.value = ""
            mensagem.value = ""
        else:
            resultado.value = "Por favor, preencha todos os campos."

        page.update()

    botao_enviar = ft.ElevatedButton(
        "Enviar",
        on_click=enviar_formulario
    )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Formulário de Contato",
                    size=24,
                    weight="bold"
                ),
                nome,
                email,
                mensagem,
                botao_enviar,
                resultado
            ],
            spacing=15
        )
    )

ft.app(target=main)