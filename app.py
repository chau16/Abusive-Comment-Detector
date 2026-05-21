import streamlit as st
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# 1. Page Setup
st.set_page_config(page_title="AI Comment Moderator", page_icon="🛡️")
st.title("🛡️ AI Comment Moderator")
st.write("Type a comment below to see if the AI flags it as abusive.")


# 2. Load the Brain (We cache this so it only loads once)
@st.cache_resource
def load_model():
    # Point this to the folder you unzipped!
    tokenizer = BertTokenizer.from_pretrained('./my_abusive_model')
    model = BertForSequenceClassification.from_pretrained('./my_abusive_model')
    return tokenizer, model


tokenizer, model = load_model()

# 3. The User Interface
user_input = st.text_area("Enter your comment here:", placeholder="e.g., You are doing a great job!")

# 4. The Action Button
if st.button("Check Comment"):
    if user_input.strip() == "":
        st.warning("Please enter some text first.")
    else:
        # Translate text to AI math
        inputs = tokenizer(user_input, return_tensors="pt", truncation=True, padding=True)

        # Make the prediction
        with torch.no_grad():
            outputs = model(**inputs)
            prediction = torch.argmax(outputs.logits, dim=1).item()

        # Show the result on the screen!
        st.markdown("### Result:")
        if prediction == 1:
            st.error("🚨 **FLAGGED:** This comment appears to be abusive.")
        else:
            st.success("✅ **CLEAN:** This comment is safe.")