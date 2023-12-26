import os
import streamlit as st
from textSummarizer.pipeline.prediction import PredictionPipeline
import time

def main():

    st.title('Text Summarization')

    text = st.text_input(label='Enter the Full Content')
    if text:
        if st.button("Generate Summary"):
            with st.spinner(text='Okay, text received by the 🔙🔚, \n bots working to generate summary for you.'):

                obj = PredictionPipeline()
                summary = obj.predict(text)
                final_sum = ""
                for i in summary:
                    if i in ['<','n',">"]:
                        final_sum +=""
                    else:
                        final_sum += i
                st.code(final_sum)
    

if __name__ == "__main__":
    main()
