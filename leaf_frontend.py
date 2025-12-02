import streamlit as st
import requests

# Local backend API URL
api_url = "http://127.0.0.1:8000"

st.title("🌿 Leaf Disease Detection")

uploaded_file = st.file_uploader("Upload a leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Preview", use_column_width=True)
    
    if st.button("🔍 Detect Disease"):
        with st.spinner("Analyzing image..."):
            try:
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                response = requests.post(f"{api_url}/disease-detection-file", files=files)
                
                if response.status_code == 200:
                    result = response.json()
                    st.write("### Result:", result)
                else:
                    st.error(f"API Error: {response.status_code}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
