#define MyAppName "ConvertFlow"
#define MyAppVersion "1.0.1"
#define MyAppPublisher "ConvertFlow"
#define MyAppExeName "ConvertFlow.exe"

[Setup]
AppId={{C0B4E6B7-2D6A-4E1B-9F0A-7E4C6E4B4F01}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppPublisher={#MyAppPublisher}
DefaultDirName={autopf}\ConvertFlow
DefaultGroupName=ConvertFlow
OutputDir=..\build\installer
OutputBaseFilename=ConvertFlow-Windows
Compression=lzma
SolidCompression=yes
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64compatible
PrivilegesRequired=admin

[Files]
Source: "..\build\windows\*"; DestDir: "{app}"; Flags: recursesubdirs ignoreversion

[Icons]
Name: "{group}\ConvertFlow"; Filename: "{app}\ConvertFlow.exe"
Name: "{autodesktop}\ConvertFlow"; Filename: "{app}\ConvertFlow.exe"

[Run]
Filename: "{app}\MicrosoftEdgeWebview2Setup.exe"; Parameters: "/silent /install"; StatusMsg: "Installing Microsoft Edge WebView2 Runtime..."; Flags: waituntilterminated
Filename: "{app}\ConvertFlow.exe"; Description: "Launch ConvertFlow"; Flags: nowait postinstall skipifsilent
