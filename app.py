import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Hello, Streamlit!")
st.write("This is your first Streamlit app. 🎉")

# Add an interactive widget
name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}! Welcome to Streamlit.")


df = pd.DataFrame({
    "Column 1": [1, 2, 3],
    "Column 2": [4, 5, 6]
})
st.write(df)


x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)
