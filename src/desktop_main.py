import webview

CONVERTFLOW_URL = "https://convertflow-seven-delta.vercel.app/"


def main() -> None:
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


if __name__ == "__main__":
    main()
