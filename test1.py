import os
import openai
import streamlit as st

st.header("Autoresponse generator to any reviews")
reviews=st.text_area("Copy Paste any customer review")
button= st.button("Autogenerate Response")

def gen_auto_response(reviews):
openai.api_key = "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"
response = openai.ChatCompletion.create(
model="text-davinci-003",
prompt="Auto response generator \n\n”Review: {reviews} \n\nReply: \n",
temperature=0.7,
max_tokens=256,
top_p=1,
frequency_penalty=0,
presence_penalty=0
)
print(response)
return response.choices[0].text
If reviews and button:
	With st.spinner(".....Generating Autoresponse to your review....."):
	Reply=gen_auto_response(reviews)
st.write(reply)
