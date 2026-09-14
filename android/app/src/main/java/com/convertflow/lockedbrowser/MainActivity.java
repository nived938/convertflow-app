package com.convertflow.lockedbrowser;

import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.view.Window;
import android.view.WindowInsets;
import android.view.WindowInsetsController;
import android.webkit.WebView;

import androidx.core.view.WindowCompat;

import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        Window window = getWindow();

        // Keep the WebView completely edge-to-edge. This lets the website's
        // top bar/background continue behind the Android status bar.
        WindowCompat.setDecorFitsSystemWindows(window, false);
        window.setStatusBarColor(Color.TRANSPARENT);
        window.setNavigationBarColor(Color.WHITE);

        // Status-bar time/icons must be WHITE. Navigation-bar icons remain dark.
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.R) {
            WindowInsetsController controller = window.getInsetsController();
            if (controller != null) {
                controller.setSystemBarsAppearance(
                    WindowInsetsController.APPEARANCE_LIGHT_NAVIGATION_BARS,
                    WindowInsetsController.APPEARANCE_LIGHT_STATUS_BARS
                        | WindowInsetsController.APPEARANCE_LIGHT_NAVIGATION_BARS
                );
            }
        } else {
            window.getDecorView().setSystemUiVisibility(
                View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR
            );
        }

        final WebView webView = getBridge().getWebView();
        webView.setFitsSystemWindows(false);
        webView.setPadding(0, 0, 0, 0);

        webView.setOnApplyWindowInsetsListener((view, insets) -> {
            int top = 0;

            if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.R) {
                android.graphics.Insets bars = insets.getInsets(
                    WindowInsets.Type.systemBars() | WindowInsets.Type.displayCutout()
                );
                top = bars.top;
            } else {
                top = insets.getSystemWindowInsetTop();
            }

            final float density = getResources().getDisplayMetrics().density;
            final int topDp = Math.round(top / density);

            // Do NOT add a margin to the WebView. The WebView must stay full
            // screen so the website header paints behind the status bar.
            webView.post(() -> applyHeaderInset(webView, topDp));
            return insets;
        });

        webView.post(() -> webView.requestApplyInsets());

        // React may create/replace the header after the first WebView layout.
        // Re-apply the inset after the page has rendered and after navigation.
        webView.postDelayed(() -> applyHeaderInset(webView, getStatusBarDp()), 400);
        webView.postDelayed(() -> applyHeaderInset(webView, getStatusBarDp()), 1200);
        webView.postDelayed(() -> applyHeaderInset(webView, getStatusBarDp()), 2500);
        webView.postDelayed(() -> applyHeaderInset(webView, getStatusBarDp()), 5000);
    }

    private int getStatusBarDp() {
        WindowInsets insets = getWindow().getDecorView().getRootWindowInsets();
        if (insets == null) {
            return 24;
        }

        int top;
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.R) {
            android.graphics.Insets bars = insets.getInsets(
                WindowInsets.Type.systemBars() | WindowInsets.Type.displayCutout()
            );
            top = bars.top;
        } else {
            top = insets.getSystemWindowInsetTop();
        }

        return Math.round(top / getResources().getDisplayMetrics().density);
    }

    private void applyHeaderInset(WebView webView, int topDp) {
        if (topDp <= 0) {
            return;
        }

        // Inject a real spacer INSIDE the website's top navigation instead of
        // shrinking/moving the WebView. The navigation background therefore
        // still fills the status-bar area, while the logo/text/menu start
        // below it, exactly like adding top padding to the website header.
        String js = "(function(){"
            + "var top='" + topDp + "px';"
            + "var candidates=Array.from(document.querySelectorAll('header,nav,[role=\\\"navigation\\\"]'));"
            + "var header=candidates.find(function(el){var r=el.getBoundingClientRect();return r.top<=5&&r.width>=window.innerWidth*0.7;});"
            + "if(!header){return;}"
            + "var old=document.getElementById('convertflow-android-inset-style');"
            + "if(old){old.remove();}"
            + "var style=document.createElement('style');"
            + "style.id='convertflow-android-inset-style';"
            + "style.textContent='#convertflow-android-header-inset{height:" + topDp + "px!important;min-height:" + topDp + "px!important;width:100%!important;display:block!important;flex:none!important;}';"
            + "document.head.appendChild(style);"
            + "var spacer=document.getElementById('convertflow-android-header-inset');"
            + "if(!spacer){spacer=document.createElement('div');spacer.id='convertflow-android-header-inset';header.insertBefore(spacer,header.firstChild);}"
            + "spacer.style.height=top;spacer.style.minHeight=top;"
            + "})();";

        webView.evaluateJavascript(js, null);
    }
}
