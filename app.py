from base64 import b64encode
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
st.set_page_config(page_title="Bishnu Kumar | Software Developer", page_icon="💻", layout="wide")

portrait = b64encode((ROOT / "assets" / "portrait.jpg").read_bytes()).decode("ascii")
page = (ROOT / "portfolio.html").read_text(encoding="utf-8")
styles = (ROOT / "style.css").read_text(encoding="utf-8")
st.html(f"<style>{styles}</style>" + page.replace("{{PORTRAIT}}", portrait))
