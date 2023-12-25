import streamlit as st
import pickle

# loading the trained model
model = pickle.load(open('model.pkl', 'rb'))

# create title
st.title('Predicting sentiment ')
review= st.text_input('Enter a review ')

submit = st.button('Predict')

if submit:
    prediction = model.predict([review])

    # print(prediction)
    # st.write(prediction)
  
