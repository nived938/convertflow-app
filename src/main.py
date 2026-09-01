import sys
import webbrowser
import flet as ft

CONVERTFLOW_URL = "https://convertflow-seven-delta.vercel.app/"


def main(page: ft.Page):
    page.title = "ConvertFlow"
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.Colors.SURFACE
    page.theme_mode = ft.ThemeMode.SYSTEM

    def open_website(_=None):
        webbrowser.open(CONVERTFLOW_URL)

    # Flet's official WebView extension currently supports Android, iOS,
    # macOS and Web, but not Windows. Windows therefore uses the system browser.
    if sys.platform == "win32":
        page.window.min_width = 420
        page.window.min_height = 700
        page.window.width = 1100
        page.window.height = 760

        page.add(
            ft.SafeArea(
                expand=True,
                content=ft.Container(
                    expand=True,
                    padding=32,
                    content=ft.Column(
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=20,
                        controls=[
                            ft.Icon(ft.Icons.SWAP_HORIZ, size=72),
                            ft.Text("ConvertFlow", size=38, weight=ft.FontWeight.BOLD),
                            ft.Text(
                                "Convert, compress and transform files online.",
                                size=17,
                                text_align=ft.TextAlign.CENTER,
                            ),
                            ft.FilledButton(
                                "Open ConvertFlow",
                                icon=ft.Icons.OPEN_IN_BROWSER,
                                on_click=open_website,
                                width=260,
                                height=52,
                            ),
                            ft.Text(
                                "The Windows app uses your default browser for the ConvertFlow web app.",
                                size=12,
                                color=ft.Colors.ON_SURFACE_VARIANT,
                                text_align=ft.TextAlign.CENTER,
                            ),
                        ],
                    ),
                ),
            )
        )
        return

    import flet_webview as fwv

    status = ft.Text("Ready", size=12, color=ft.Colors.ON_SURFACE_VARIANT)

    def set_status(value: str):
        status.value = value
        page.update()

    webview = fwv.WebView(
        url=CONVERTFLOW_URL,
        expand=True,
        on_page_started=lambda e: set_status("Loading ConvertFlow…"),
        on_page_ended=lambda e: set_status("Ready"),
        on_web_resource_error=lambda e: set_status("Unable to load a page. Check your connection."),
    )

    async def go_back(_):
        try:
            if await webview.can_go_back():
                await webview.go_back()
        except Exception:
            pass

    async def go_forward(_):
        try:
            if await webview.can_go_forward():
                await webview.go_forward()
        except Exception:
            pass

    async def reload(_):
        try:
            await webview.reload()
        except Exception:
            pass

    toolbar = ft.Container(
        padding=ft.padding.symmetric(horizontal=8, vertical=6),
        content=ft.Row(
            controls=[
                ft.IconButton(ft.Icons.ARROW_BACK, tooltip="Back", on_click=go_back),
                ft.IconButton(ft.Icons.ARROW_FORWARD, tooltip="Forward", on_click=go_forward),
                ft.IconButton(ft.Icons.REFRESH, tooltip="Reload", on_click=reload),
                ft.Container(expand=True),
                status,
            ]
        ),
    )

    page.add(
        ft.SafeArea(
            expand=True,
            content=ft.Column(
                expand=True,
                spacing=0,
                controls=[toolbar, ft.Divider(height=1), webview],
            ),
        )
    )


if __name__ == "__main__":
    ft.run(main)
