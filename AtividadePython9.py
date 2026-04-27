import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.window_width = 400
    page.window_height = 500

    campo_tarefa = ft.TextField(
        label="Digite uma tarefa",
        width=300
    )

    lista_tarefas = ft.Column()

    def adicionar_tarefa(e):
        if campo_tarefa.value.strip() != "":
            lista_tarefas.controls.append(
                ft.Text(f"• {campo_tarefa.value}")
            )
            campo_tarefa.value = ""
            page.update()


    botao_adicionar = ft.ElevatedButton(
        "Adicionar",
        on_click=adicionar_tarefa
    )

    page.add(
        ft.Text("Lista de Tarefas", size=24, weight="bold"),
        campo_tarefa,
        botao_adicionar,
        ft.Divider(),
        lista_tarefas
    )

ft.app(target=main)