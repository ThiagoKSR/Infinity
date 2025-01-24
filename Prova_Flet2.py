import flet as ft

def main(page: ft.Page):
    def button_clicked(e):
        t.value = f"Os seguintes dados foram enviados: \n{tb2.value}\n{tb3.value}\n{tb4.value}."
        page.update()

    t = ft.Text()

    tb2 = ft.TextField(label="Nome completo:", disabled=False,bgcolor=ft.colors.BLACK, color=ft.colors.WHITE)
    tb3 = ft.TextField(label="Seu melhor email:", read_only=False, bgcolor=ft.colors.BLACK, color=ft.colors.WHITE)
    tb4 = ft.TextField(label="Digite aqui um breve motivo do seu contato:", bgcolor=ft.colors.BLACK, color=ft.colors.WHITE)
    b2 = ft.ElevatedButton(text="Enviar", on_click=button_clicked)
    page.add(tb2, tb3, tb4, t, b2)


ft.app(main)