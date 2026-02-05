import flet as ft


def carga_form():

    txt_codigo = ft.TextField(label="Código")
    txt_cantidad = ft.TextField(label="Cantidad", keyboard_type=ft.KeyboardType.NUMBER)
    dd_ubicacion = ft.Dropdown(
        label="Ubicación",
        options=[
            ft.dropdown.Option("Producción"),
            ft.dropdown.Option("Mecanizado"),
            ft.dropdown.Option("Calidad"),
        ]
    )
    boton = ft.ElevatedButton(
        content=ft.Text("Guardar Registro", color="white"),
        bgcolor="#1976D2",
        width=300
    )
    #bar_navegacion= ft.NavigationBar = ft.NavigationBarDestination(
    # destinations=[
    #       ft.NavigationBarDestination(icon=ft.Icons.ADD_BOX, label="Carga"),
    #      ft.NavigationBarDestination(icon=ft.Icons.BAR_CHART, label="Gráficos"),
    # ],
    #)


    vista = ft.Column( # lo que veremos ( lo acomoda uno debajo del otro )
        controls=[
            ft.Text("EMPRESA - CARGA", size=20, weight="bold"),
            txt_codigo,
            txt_cantidad,
            dd_ubicacion,
            boton,

        ],
        spacing=12
    )
    horizontal_alignment = ft.CrossAxisAlignment.CENTER
    alignment = ft.MainAxisAlignment.CENTER
    # Devolvemos la vista y los widgets si queremos usarlos fuera
    return vista
