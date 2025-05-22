import json
from pathlib import Path

# credentials.json を読み込む
with open("credentials.json", "r", encoding="utf-8") as f:
    creds = json.load(f)

# .streamlit ディレクトリを作成
streamlit_dir = Path(".streamlit")
streamlit_dir.mkdir(exist_ok=True)

# secrets.toml を書き出し
secrets_path = streamlit_dir / "secrets.toml"
with open(secrets_path, "w", encoding="utf-8") as f:
    f.write("[gdrive]\n")
    for key, value in creds.items():
        if isinstance(value, str):
            value = value.replace("\n", "\\n")  # ダブルエスケープ
        f.write(f'{key} = "{value}"\n')

print("✅ .streamlit/secrets.toml を作成しました")
