"""
Vaigai North Bank Road Project — Home
"""
import streamlit as st
from shared_data import get_available_files, get_selected_data_file

st.title("Vaigai North Bank Road Project")
st.markdown("**Analytics Dashboard**")

st.divider()

st.subheader("Select data source")
available = get_available_files()
file_opt = [fname for fname, _ in available]
label_opt = [label for _, label in available]
current = get_selected_data_file()
idx = file_opt.index(current) if current in file_opt else 0
idx = min(idx, len(file_opt) - 1) if file_opt else 0

sel = st.selectbox(
    "Data file",
    options=file_opt,
    format_func=lambda x: label_opt[file_opt.index(x)] if x in file_opt else x,
    index=idx,
    key="home_data_select",
)
st.session_state["selected_data_file"] = sel

st.info(f"**Viewing:** {label_opt[file_opt.index(sel)]} — all pages use this data.")

st.divider()
st.markdown("""
Welcome to the Vaigai North Bank Road Project dashboard. Use the **sidebar** to navigate:
- **Mbook** — Mbook pages and date analysis
- **Progress** — Month-wise length progress
- **Overlap & Gap** — Stretch-wise overlap and gap analysis
- **Timeline** — Date × Item charts and timeline by estimate
""")
