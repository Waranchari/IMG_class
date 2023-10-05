import streamlit as st
from transformers import pipeline
from PIL import Image

pipeline = pipeline(task="image-classification", model="microsoft/resnet-50")

def predict(image):
    predictions = pipeline(image)
    return {p["label"]: p["score"] for p in predictions}

def main():
    st.title("Image Classification")
    
    with st.form("my_form"):
        uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
        # Display the uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
        clicked = st.form_submit_button("Predict")
        if clicked:
            col1, col2, col3, col4, col5 = st.columns(5)
            results = predict(image)
            k = [] 
            v = []
            for key, value in my_dict.items():
                value = round(value*100,2)
                v.append(value)
                k.append(key)
            with col1:
                st.header(k[0],divider='red')
                st.subheader(v[0])
            with col2:
                st.header(k[1],divider='red')
                st.subheader(v[1])
            with col3:
                st.header(k[2],divider='red')
                st.subheader(v[2])
            with col4:
                st.header(k[3],divider='red')
                st.subheader(v[3])
            with col5:
                st.header(k[4],divider='red')
                st.subheader(v[4])

if __name__ == "__main__":
    main()