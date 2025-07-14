# UE5-HDR-Test-Images
UE5用HDR調整画像と生成ツール

## ✅ 概要
Unreal Engine 5 の `r.HDR.Display.*` 系パラメータ調整用の .exr HDR画像と生成スクリプトです。

## 📂 ファイル内容

- `ue5_hdr_max_400_1000.exr`  
　最大輝度（400〜1000nit）テスト画像

- `ue5_hdr_min_log10_-1.5_-4.0.exr`  
　最小輝度（log10 -1.5〜-4.0 ≒ 0.03〜0.0001 nit）テスト画像

- `generate_hdr_exr.py`  
　これらの画像を生成するスクリプト（Python）

## 🛠 使用方法

1. `.exr` ファイルを Unreal Engine に読み込む
2. `Post Process Volume` にテスト画像を配置
3. 暗部・明部の再現性を確認しながら下記パラメータを調整：

```ini
r.HDR.Display.MaxLuminance=1000
r.HDR.Display.MinLuminanceLog10=-3.0
