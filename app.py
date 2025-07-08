import streamlit as st
from workflows.process_fica_documents import run_full_pipeline

st.set_page_config(page_title="AI FICA Agent", layout="centered")

st.title("📑 AI FICA Agent")
st.write("Upload your ID and Proof of Residence below.")

uploaded_id = st.file_uploader("Upload ID Document (PDF)", type=["pdf"])
uploaded_por = st.file_uploader("Upload Proof of Residence (PDF)", type=["pdf"])

if st.button("Run Compliance Check"):
    if uploaded_id and uploaded_por:
        with st.spinner("Analyzing documents..."):
            result = run_full_pipeline(uploaded_id, uploaded_por)
            st.success(result["status"])
            st.write("### Summary")
            st.json(result["summary"])
            st.write("### STR Draft")
            st.code(result["str_draft"])
    else:
        st.error("Please upload both documents.")
