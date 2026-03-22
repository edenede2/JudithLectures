"""
Streamlit app for translating Hebrew PowerPoint presentations to English.

Usage:
    streamlit run app.py
"""

import streamlit as st
from pptx_translator import (
    generate_template_from_bytes,
    translate_pptx_bytes,
    get_chatgpt_prompt,
)

st.set_page_config(page_title="PPTX Translator")
st.title(" Hebrew \u2192 English PPTX Translator")

# ─── Step 1: Generate Template ────────────────────────────────

st.header("Step 1: Generate Template")
st.markdown("Upload your **.pptx** file to get a translation template and a ChatGPT prompt.")

pptx_file = st.file_uploader("Upload PPTX", type=["pptx"], key="tmpl_upload")

# Generate template automatically when file is uploaded
if pptx_file is not None:
    # Cache in session_state so it survives re-runs / downloads
    if (
        "template" not in st.session_state
        or st.session_state.get("tmpl_file_name") != pptx_file.name
    ):
        pptx_bytes = pptx_file.read()
        st.session_state["template"] = generate_template_from_bytes(
            pptx_bytes, "Hebrew", "English"
        )
        st.session_state["prompt"] = get_chatgpt_prompt("Hebrew", "English")
        st.session_state["tmpl_file_name"] = pptx_file.name

    st.success("Template ready!")

    st.subheader("ChatGPT Prompt")
    st.info(
        "1. Copy the prompt below and paste it into ChatGPT.\n"
        "2. Attach the **PDF** of your presentation.\n"
        "3. Attach the **template.md** file (download below).\n"
        "4. Save ChatGPT\u2019s response as a `.md` file.\n"
        "5. Go to **Step 2** below."
    )
    st.code(st.session_state["prompt"], language="text")

    st.subheader("Translation Template")
    st.download_button(
        "\u2B07\uFE0F Download template.md",
        st.session_state["template"],
        file_name="template.md",
        mime="text/markdown",
    )
    with st.expander("Preview template"):
        st.code(st.session_state["template"], language="markdown")

# ─── Step 2: Apply Translation ────────────────────────────────

st.divider()
st.header("Step 2: Apply Translation")
st.markdown("Upload the **original PPTX** and the **translated .md** from ChatGPT.")

orig_pptx = st.file_uploader("Original PPTX", type=["pptx"], key="orig_upload")
trans_md = st.file_uploader("Translated MD", type=["md", "txt"], key="md_upload")

if orig_pptx is not None and trans_md is not None:
    if st.button("Translate ", type="primary"):
        with st.spinner("Translating..."):
            pptx_bytes = orig_pptx.read()
            md_text = trans_md.read().decode("utf-8")
            output_bytes, warnings = translate_pptx_bytes(
                pptx_bytes, md_text,
                src_lang_code="he-IL",
                tgt_lang_code="en-US",
            )
            st.session_state["output_bytes"] = output_bytes
            st.session_state["output_warnings"] = warnings
            st.session_state["output_name"] = orig_pptx.name.replace(
                ".pptx", "_EN.pptx"
            )

    if "output_bytes" in st.session_state:
        warnings = st.session_state["output_warnings"]
        if warnings:
            with st.expander(f"\u26A0\uFE0F {len(warnings)} warning(s)"):
                for w in warnings:
                    st.warning(w)

        st.success("Done!")
        st.download_button(
            f"\u2B07\uFE0F Download {st.session_state['output_name']}",
            st.session_state["output_bytes"],
            file_name=st.session_state["output_name"],
            mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
        )
