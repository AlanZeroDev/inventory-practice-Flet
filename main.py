import flet as ft

#main recibe parametro una page de flet
def main(page: ft.Page):
    page.title= "Gestion Stock" #titulo
    page.window_width = 400 # ancho
    page.window_height = 700 #alto
    page.padding = 10 #borde
    page.theme_mode = ft.ThemeMode.LIGHT #tema color
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER #central elementos

    page.appbar = ft.AppBar(   # barra superior
        title=ft.Text("App Empresa"),
        center_title=False,
        bgcolor="#1976D2"
    )

    txt_codigo = ft.TextField(label="Código") #crear un imput y adentro tendra "codigo"
    txt_cantidad = ft.TextField(  # lo mismo pero con cantidad
        label="B - Cantidad",
        keyboard_type=ft.KeyboardType.NUMBER
    )
    dd_ubicacion = ft.Dropdown( # elejir una opcion de la lista
        label="C - Ubicación",
        options=[
            ft.dropdown.Option("Producción"),
            ft.dropdown.Option("Mecanizado"),
            ft.dropdown.Option("Calidad"),
        ]
    )
    buttom = ft.ElevatedButton( # boton con "guardar registro"
        content=ft.Text("Guardar Registro", color="white"),
        bgcolor="#1976D2",
        width=300
    )

    vista_carga = ft.Column( #columna ordena uno debajo del otro
        controls=[
            ft.Text("EMPRESA - CARGA", size=20, weight="bold"),
            txt_codigo,
            txt_cantidad,
            dd_ubicacion,
            buttom,
        ],
        visible=True,
        spacing=12
    )


    page.add(vista_carga)
ft.run(main) #correr app iniciando en main

#