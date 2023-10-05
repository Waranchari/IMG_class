import pandas as pd
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
            results = predict(image)
            k = [] 
            v = []
            for key, value in results.items():
                value = round(value*100,2)
                v.append(value)
                k.append(key)
            vp = [str(item) + '%' for item in v]
            df = pd.DataFrame({'Predict Value': k,'Accuracy':vp})
            st.dataframe(df,hide_index=True)

if __name__ == "__main__":
    main()