import flet as ft

def main(page: ft.Page):
    page.title = "Inicio de sesion"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    icono = ft.Icon(
        icon=ft.Icons.PERSON,
        color="purple200",
        size=60
    )
    page.add(icono)

    
    sesion = ft.Container(
        width=350,
        padding=30,
        border_radius=10,
        bgcolor="Grey200",
        
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15,
            controls=[
                
                
                ft.Text("Iniciar sesión", size=40, weight="bold"),

                ft.TextField(
                    label="Correo electrónico",
                    width=280,
                ),

                ft.TextField(
                    label="Introduzca su contraseña",
                    password=True,
                    can_reveal_password=True,
                    width=280
                ),

                ft.Button(
                    content="Iniciar sesion",
                    width=280,
                    color="white",
                    bgcolor="purple200",
                    
                ),
                
                ft.TextButton(
                content="¿Olvidaste tu contraseña?",
                icon_color=ft.Colors.BLUE_300,
)
            ]
        )
    )

    page.add(sesion)

ft.app(target=main)
