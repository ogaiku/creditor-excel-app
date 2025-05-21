# 債務者別 債権者一覧Excel出力アプリ

このアプリは、JSON形式で債権者情報を読み込み、債務者単位で分類・管理し、テンプレートExcelに出力できるStreamlitアプリです。

## 利用方法

1. 必要ライブラリのインストール
```
pip install -r requirements.txt
```

2. アプリの起動
```
streamlit run app.py
```

3. 内部テンプレート（`internal_template.xlsx`）をこのディレクトリに配置しておく必要があります。

## 出力形式

- ファイル名: `<債務者名>_fields_master.xlsx`
- 出力内容: 債務者に紐づく債権者一覧をテンプレートExcelに記載
