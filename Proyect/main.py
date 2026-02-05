import flet as ft
from Proyect.Pantallas.pantallaCargaDatos import carga_form
from Proyect.Pantallas.pantallaGraficos import carga_Graficos

def main(page: ft.Page):
    page.title = "Gestion Stock" # Titulo pagina
    page.window_width = 400# tamaño
    page.window_height = 700#tamaño
    page.theme_mode = ft.ThemeMode.LIGHT # tema
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER #centramos todo
    page.vertical_alignment = ft.MainAxisAlignment.CENTER # centramos todo

    # 1. Se cargan las vistas
    vista_carga = carga_form()
    vista_datos = carga_Graficos()


    # 2. Defino contenedor y signo la vista inicial

    cuerpo_de_la_app = ft.Container(content=vista_carga, expand=True)

    #3. Barra de navegacion
    def on_navigation_change(e):
        index = e.control.selected_index
        if index == 0:
            cuerpo_de_la_app.content = vista_carga
        elif index == 1:
            cuerpo_de_la_app.content = vista_datos

        page.update()

    page.appbar = ft.AppBar( # barra de arriba del todo
        title=ft.Text("App Empresa"),
        bgcolor="#1976D2"
    )

    # 4. Asignamos la barra directamente a la propiedad de la página
    page.navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=on_navigation_change,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
            ft.NavigationBarDestination(icon=ft.Icons.SEARCH, label="Gráficos"),
        ],
        bgcolor="#1976D2",
        indicator_color=ft.Colors.AMBER,
    )

    # 4. Mostramos el contenedor que tiene toda la data
    page.add(cuerpo_de_la_app)


ft.run(main)