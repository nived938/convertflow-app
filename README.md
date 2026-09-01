# ConvertFlow App

A Python-based cross-platform app for [ConvertFlow](https://convertflow-seven-delta.vercel.app/).

## Platforms

- Windows: installer EXE. The app opens ConvertFlow in the system browser because the official Flet WebView extension does not currently support Windows.
- Android: APK with an embedded ConvertFlow WebView.
- macOS: DMG with an embedded ConvertFlow WebView.
- iOS: signed IPA when Apple Developer signing secrets are configured in GitHub Actions.

## Download latest builds

After the first tagged release is published, the stable download URLs are:

- `https://github.com/nived938/convertflow-app/releases/latest/download/ConvertFlow-Windows.exe`
- `https://github.com/nived938/convertflow-app/releases/latest/download/ConvertFlow-Android.apk`
- `https://github.com/nived938/convertflow-app/releases/latest/download/ConvertFlow-Ios.ipa`
- `https://github.com/nived938/convertflow-app/releases/latest/download/ConvertFlow-Mac.dmg`

## Release

Push a semantic version tag such as `v1.0.0` to start the Windows, Android and macOS builds and publish them to GitHub Releases.

```bash
git tag v1.0.0
git push origin v1.0.0
```

### iOS signing

An installable IPA cannot be produced without Apple signing credentials. GitHub Actions expects these repository secrets:

- `APPLE_CERTIFICATE_BASE64`
- `APPLE_CERTIFICATE_PASSWORD`
- `IOS_PROVISION_PROFILE_BASE64`
- `IOS_TEAM_ID`
- `IOS_SIGNING_CERTIFICATE`
- `IOS_PROVISIONING_PROFILE`

The iOS job can then build a signed testing IPA and upload it to the release.
