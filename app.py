import streamlit as st
from transformers import pipeline
from Pillow import Image

pipeline = pipeline(task="image-classification", model="microsoft/resnet-50")

def predict(image):
    predictions = pipeline(image)
    return {p["label"]: p["score"] for p in predictions}

def main():
    st.title("Image Classification")
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        clicked = st.form_submit_button("Predict")
        if clicked:
            results = predict(image)
            sorted_data = sorted(results, reverse=True)
            top_five = sorted_data[:5]
            st.success('The predicted image is {}'.format(top_five))

if __name__ == "__main__":
    main()