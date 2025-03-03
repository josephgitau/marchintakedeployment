# import libraries
import streamlit as st

# give your app a title
st.title("Model Deployment Web app")

# st.header
st.header('Loan prediction Web app')

# paragraphs of info
st.write('This is a web created using streamlit for loan predictions. The app is supposed to take in user information and predict if an individual qualifies for a loan or not.')

st.markdown('This is a project implemented by the march intake africdsa students. `streamlit web app`')

st.subheader('Data Info')
st.text('Some info on the loan data')

# model formula
st.text('Base model will be a linear regression equation with the formula shown below')
st.latex(r"y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_n x_n + \epsilon")
st.caption('Equation 1: Linear regression equation')
