import streamlit as st
import pandas as pd
import json
import shutil
import tempfile
from pathlib import Path
from io import BytesIO

TEMPLATE_PATH = Path("internal_template.xlsx")

st.set_page_config(page_title="債務者別Excel出力", layout="wide")
st.title("債務者別 債権者一覧Excel出力アプリ")

if "uploaded_data" not in st.session_state:
    st.session_state.uploaded_data = []

json_file = st.file_uploader("債権者データ（JSON）をアップロード", type="json")
if json_file:
    data = json.load(json_file)
    if isinstance(data, dict): data = [data]
    st.session_state.uploaded_data.extend(data)
    st.success(f"{len(data)} 件のデータを追加しました。")

if st.session_state.uploaded_data:
    df_all = pd.DataFrame(st.session_state.uploaded_data)
    debtor_names = df_all["debtor_name"].dropna().unique().tolist()
    selected_debtor = st.selectbox("債務者を選択", debtor_names)

    df_debtor = df_all[df_all["debtor_name"] == selected_debtor]
    st.dataframe(df_debtor)

    def make_excel(debtor, df):
        with tempfile.TemporaryDirectory() as tmpdir:
            file_name = f"{debtor.replace(' ', '')}_fields_master.xlsx"
            output_path = Path(tmpdir) / file_name
            shutil.copy(TEMPLATE_PATH, output_path)
            with pd.ExcelWriter(output_path, engine="openpyxl", mode="a", if_sheet_exists="overlay") as writer:
                df.to_excel(writer, index=False, sheet_name="債権者一覧", startrow=1)
            return BytesIO(open(output_path, "rb").read())

    if st.button("📥 Excelダウンロード"):
        excel = make_excel(selected_debtor, df_debtor)
        st.download_button("⬇ ダウンロード", data=excel, file_name=f"{selected_debtor}_fields_master.xlsx")
