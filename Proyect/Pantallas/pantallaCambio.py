#import flet as ft

def on_navigation_change(e):
   selected_index = e.control.selected_index
   if selected_index == 0:
        main()
        ft.update()

