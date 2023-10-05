import streamlit as st
from transformers import pipeline

pipe = pipeline("question-answering", model="deepset/roberta-base-squad2")
def main():
    st.title("Yelp review")

    with st.form("text_field"):
        text = st.text_area('enter some text:')
        # clicked==True only when the button is clicked
        clicked = st.form_submit_button("Submit text")
        if clicked:
          results = pipe([text])
          st.json(results)

if __name__ == "__main__":
    main()