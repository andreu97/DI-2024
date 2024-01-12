import flet as ft
class App:
    def __init__(self) -> None:
        ft.app(target=self.main,view="web_browser",port=8080)
        
    def main(self,page: ft.Page):
        self.page=page
        page.title = "Andreu Albors"
        page.theme_mode = ft.ThemeMode.LIGHT
        page.padding = 50
        page.update()

        images = ft.GridView(
            expand=1,
            runs_count=5,
            max_extent=150,
            child_aspect_ratio=1.0,
            spacing=5,
            run_spacing=5,
        )

        page.add(images)

        for i in range(1, 26):
            images.controls.append(
                
                    ft.Container(
                        content=ft.Text(value=str(i)),
                        alignment=ft.alignment.center,
                        width=200,
                        height=200,
                        bgcolor=ft.colors.AMBER,
                        border_radius=ft.border_radius.all(5),
                    )
                
            )
        page.update()

if __name__=="__main__":
    app=App()
