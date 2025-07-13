import streamlit as st
import streamlit.components.v1 as components
powerbi_embed_url = "https://app.powerbi.com/view?r=eyJrIjoiNDFlZGE5NmQtMzIyYy00NzYxLTkwZTktNjBlNTlkMTQ2NjAyIiwidCI6ImY2YmI1MjU3LTE1ZTEtNGUxYi1iY2U0LTNjNTVmMjEyNjU3MSJ9"
st.markdown(
    f"""
    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
        <iframe src="{powerbi_embed_url}" 
                style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;" 
                allowfullscreen="true">
        </iframe>
    </div>
    """,
    unsafe_allow_html=True
)

if st.button("Send balloons!"):
    st.balloons()
