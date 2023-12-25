import os
import streamlit as st
from textSummarizer.pipeline.prediction import PredictionPipeline
import time

def main():

    st.title('Text Summarization')

    text = st.text_input(label='Enter the Full Content')
    
    with st.spinner(text="Hey, hope you are doing good!"):
        time.sleep(15)
        with st.spinner(text="Yeah, lemme read it for you"):
            time.sleep(25)
            with st.spinner(text="Almost Done!"):
                if st.button("Generate Summary"):
                    obj = PredictionPipeline()
                    summary = obj.predict(text)
                    st.write(summary)
    
    

if __name__ == "__main__":
    main()
