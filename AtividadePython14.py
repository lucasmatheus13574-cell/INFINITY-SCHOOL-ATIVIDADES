import flet as ft
from datetime import datetime



class Cliente:
    contador_id = 1

    def __init__(self, nome, telefone, email):
        self.id = Cliente.contador_id
        Cliente.contador_id += 1
        self.nome = nome
        self.telefone = telefone
        self.email = email


class Quarto:
    def __init__(self, numero, tipo, preco_diaria):
        self.numero = numero
        self.tipo = tipo
        self.preco_diaria = preco_diaria
        self.disponivel = True


class Reserva:
    def __init__(self, cliente, quarto, checkin, checkout):
        self.cliente = cliente
        self.quarto = quarto
        self.checkin = checkin
        self.checkout = checkout
        self.status = "Ativa"


class GerenciadorDeReservas:
    def __init__(self):
        self.clientes = []
        self.quartos = []
        self.reservas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def verificar_disponibilidade(self):
        return [q for q in self.quartos if q.disponivel]

    def criar_reserva(self, cliente, quarto, checkin, checkout):
        if quarto.disponivel:
            reserva = Reserva(cliente, quarto, checkin, checkout)
            self.reservas.append(reserva)
            quarto.disponivel = False
            return reserva
        return None

    def cancelar_reserva(self, reserva):
        reserva.status = "Cancelada"
        reserva.quarto.disponivel = True




def main(page: ft.Page):
    page.title = "Refúgio dos Sonhos - Sistema de Reservas"
    page.window_width = 900
    page.window_height = 700
    page.scroll = "auto"

    sistema = GerenciadorDeReservas()

    sistema.adicionar_quarto(Quarto(101, "Single", 150.00))
    sistema.adicionar_quarto(Quarto(102, "Double", 250.00))
    sistema.adicionar_quarto(Quarto(201, "Suite", 450.00))



    nome_cliente = ft.TextField(label="Nome")
    telefone_cliente = ft.TextField(label="Telefone")
    email_cliente = ft.TextField(label="E-mail")

    lista_clientes = ft.Column()

    def atualizar_clientes():
        lista_clientes.controls.clear()
        for c in sistema.clientes:
            lista_clientes.controls.append(
                ft.Text(f"ID: {c.id} | {c.nome} | {c.telefone} | {c.email}")
            )
        page.update()

    def salvar_cliente(e):
        if nome_cliente.value and telefone_cliente.value and email_cliente.value:
            cliente = Cliente(
                nome_cliente.value,
                telefone_cliente.value,
                email_cliente.value
            )
            sistema.adicionar_cliente(cliente)
            nome_cliente.value = ""
            telefone_cliente.value = ""
            email_cliente.value = ""
            atualizar_clientes()



    cliente_dropdown = ft.Dropdown(label="Cliente")
    quarto_dropdown = ft.Dropdown(label="Quarto")
    checkin_field = ft.TextField(label="Check-in (dd/mm/aaaa)")
    checkout_field = ft.TextField(label="Check-out (dd/mm/aaaa)")

    lista_reservas = ft.Column()

    def atualizar_dropdowns():
        cliente_dropdown.options = [
            ft.dropdown.Option(str(c.id), f"{c.nome} (ID {c.id})")
            for c in sistema.clientes
        ]

        quarto_dropdown.options = [
            ft.dropdown.Option(str(q.numero), f"Quarto {q.numero} - {q.tipo}")
            for q in sistema.verificar_disponibilidade()
        ]
        page.update()

    def atualizar_reservas():
        lista_reservas.controls.clear()

        for r in sistema.reservas:
            def cancelar_factory(reserva):
                return lambda e: cancelar_reserva(reserva)

            lista_reservas.controls.append(
                ft.Row([
                    ft.Text(
                        f"Cliente: {r.cliente.nome} | Quarto: {r.quarto.numero} | "
                        f"{r.checkin} até {r.checkout} | Status: {r.status}"
                    ),
                    ft.ElevatedButton(
                        "Cancelar",
                        on_click=cancelar_factory(r)
                    )
                ])
            )
        page.update()

    def criar_reserva(e):
        if not cliente_dropdown.value or not quarto_dropdown.value:
            return

        cliente = next(
            c for c in sistema.clientes if str(c.id) == cliente_dropdown.value
        )

        quarto = next(
            q for q in sistema.quartos if str(q.numero) == quarto_dropdown.value
        )

        sistema.criar_reserva(
            cliente,
            quarto,
            checkin_field.value,
            checkout_field.value
        )

        checkin_field.value = ""
        checkout_field.value = ""
        atualizar_dropdowns()
        atualizar_reservas()

    def cancelar_reserva(reserva):
        sistema.cancelar_reserva(reserva)
        atualizar_dropdowns()
        atualizar_reservas()



    lista_quartos = ft.Column()

    def atualizar_quartos():
        lista_quartos.controls.clear()
        for q in sistema.quartos:
            status = "Disponível" if q.disponivel else "Ocupado"
            lista_quartos.controls.append(
                ft.Text(
                    f"Quarto {q.numero} | {q.tipo} | R$ {q.preco_diaria:.2f} | {status}"
                )
            )
        page.update()


    page.add(
        ft.Text("Refúgio dos Sonhos", size=28, weight="bold"),

        ft.Divider(),
        ft.Text("Tela Inicial - Quartos", size=20),
        lista_quartos,

        ft.Divider(),
        ft.Text("Gerenciamento de Clientes", size=20),
        nome_cliente,
        telefone_cliente,
        email_cliente,
        ft.ElevatedButton("Adicionar Cliente", on_click=salvar_cliente),
        lista_clientes,

        ft.Divider(),
        ft.Text("Formulário de Reserva", size=20),
        cliente_dropdown,
        quarto_dropdown,
        checkin_field,
        checkout_field,
        ft.ElevatedButton("Criar Reserva", on_click=criar_reserva),

        ft.Divider(),
        ft.Text("Visualização de Reservas", size=20),
        lista_reservas,
    )

    atualizar_clientes()
    atualizar_dropdowns()
    atualizar_reservas()
    atualizar_quartos()


ft.app(target=main)
