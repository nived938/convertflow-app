import sys
import webview

CONVERTFLOW_URL = "https://convertflow-seven-delta.vercel.app/"


def main() -> None:
    """Launch ConvertFlow inside the native desktop application window."""
    webview.create_window(
        title="ConvertFlow",
        url=CONVERTFLOW_URL,
        width=1200,
        height=820,
        min_size=(900, 620),
        text_select=True,
        confirm_close=True,
        zoomable=True,
    )

    if sys.platform == "win32":
        webview.start(gui="edgechromium", debug=False)
    elif sys.platform == "darwin":
        webview.start(gui="cocoa", debug=False)
    else:
        webview.start(debug=False)


if __name__ == "__main__":
    main()
