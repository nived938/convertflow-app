package com.convertflow.lockedbrowser;

import android.graphics.Color;
import android.os.Bundle;
import android.view.Window;
import android.view.WindowInsetsController;

import androidx.core.view.WindowCompat;

import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        Window window = getWindow();

        // Keep the WebView below the Android status bar instead of drawing
        // underneath it. This prevents the website's top navigation from
        // being hidden behind the phone's status-bar area.
        WindowCompat.setDecorFitsSystemWindows(window, true);
        window.setStatusBarColor(Color.WHITE);
        window.setNavigationBarColor(Color.WHITE);

        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.R) {
            WindowInsetsController controller = window.getInsetsController();
            if (controller != null) {
                controller.setSystemBarsAppearance(
                    WindowInsetsController.APPEARANCE_LIGHT_STATUS_BARS
                        | WindowInsetsController.APPEARANCE_LIGHT_NAVIGATION_BARS,
                    WindowInsetsController.APPEARANCE_LIGHT_STATUS_BARS
                        | WindowInsetsController.APPEARANCE_LIGHT_NAVIGATION_BARS
                );
            }
        } else {
            window.getDecorView().setSystemUiVisibility(
                android.view.View.SYSTEM_UI_FLAG_LIGHT_STATUS_BAR
                    | android.view.View.SYSTEM_UI_FLAG_LIGHT_NAVIGATION_BAR
            );
        }
    }
}
