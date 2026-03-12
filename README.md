# Marker
PySide6 製のシンプルな Markdown エディタです。ライブプレビューを備え、まずは Typora 代替として Windows 向けに開発しています。

## 機能 (進捗)
- [x] ライブプレビュー
- [ ] ファイル読み込み/保存
- [ ] 印刷
- [ ] カスタム CSS
- [ ] シンタックスハイライト
- [ ] 拡張機能

## 必要環境
- Windows 10/11
- Python 3.13
- 主要依存: PySide6, markdown (python-markdown), PyInstaller(ビルド用)

## セットアップ
```powershell
python -m venv .venv
.\.venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install .
```

## 起動
```powershell
python main.py
```

## UI を変更したら
`ui/mainwindow.ui` を編集した後、Qt Designer の変更を Python コードに反映します。
```powershell
./compile_ui.ps1
```

## ビルド (実行ファイル作成)
PyInstaller で単一 exe を生成します。
```powershell
./compile.ps1
```
成果物は `dist/Marker.exe` に出力されます。

## スクリーンショット
![Marker markdown editor interface with dark left panel showing heading and Japanese text, and white right preview panel displaying rendered markdown output](./screenshots/main_ui.png)

## ダウンロード
Release ページからZIPを取得してください。
