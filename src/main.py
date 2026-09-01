import sys
import flet as ft

CONVERTFLOW_URL = "https://convertflow-seven-delta.vercel.app/"


def launch_desktop_webview() -> None:
    """Run ConvertFlow inside the desktop app window, not the system browser."""
    import webview

    webview.create_window(
        title="ConvertFlow",
        url=CONVERTFLOW_URL,
        width=1200,
        height=820,
        min_size=(900, 620),
        text_select=True,
        confirm_close=True,
    )
    webview.start(debug=False)


def main(page: ft.Page):
    page.title = "ConvertFlow"
    page.padding = 0
    page.spacing = 0
    page.bgcolor = ft.Colors.SURFACE
    page.theme_mode = ft.ThemeMode.SYSTEM

    import flet_webview as fwv

    status = ft.Text("Ready", size=12, color=ft.Colors.ON_SURFACE_VARIANT)

    def set_status(value: str):
        status.value = value
        page.update()

    webview = fwv.WebView(
        url=CONVERTFLOW_URL,
        expand=True,
        on_page_started=lambda e: set_status("Loading ConvertFlow..."),
        on_page_ended=lambda e: set_status("Ready"),
        on_web_resource_error=lambda e: set_status("Unable to load the page. Check your connection."),
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
    if sys.platform in ("win32", "darwin"):
        launch_desktop_webview()
    else:
        ft.run(main)
