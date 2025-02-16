import streamlit as st

# Set page config for better appearance
st.set_page_config(page_title="Simple Streamlit App", layout="centered")

# Title of the application
st.title("Simple Streamlit Application")

# Input text box
name = st.text_input("Enter your name:")

# Button to trigger greeting
if st.button("Greet Me"):
    st.success(f"Hello, {name}! Welcome to Streamlit 🚀")
st.slider("AGE:")
display = ("male", "female")
options = list(range(len(display)))
value = st.selectbox("gender", options, format_func=lambda x: display[x])
st.write(value)
ques = st.radio(
    "Do you like coding?",
    ('Yes','No'))
if ques == 'Yes':
    st.write('You like coding.')
else:
    st.write("You do not like coding.")

