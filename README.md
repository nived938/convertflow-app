# ConvertFlow Android Locked Browser

This repository contains the Android build of ConvertFlow. It opens the official service at `https://convertflow-seven-delta.vercel.app/` in a native Capacitor WebView.

## Behavior

- The destination is fixed in `capacitor.config.ts`.
- The app has no address bar, URL field, or in-app navigation controls, so the destination is not exposed for editing.
- HTTPS is required; cleartext traffic is disabled.
- The website source repository has been updated so `/admin` and nested `/admin/*` paths render the public 404 page.

## Build

```bash
npm ci
npm run build
npx cap sync android
cd android
./gradlew assembleDebug
```

The debug APK is generated at `android/app/build/outputs/apk/debug/app-debug.apk`.

## Notes

This is a kiosk-style wrapper, not a general-purpose browser. Website navigation remains inside the WebView, and the Android system back action is the only navigation affordance supplied by the platform.
