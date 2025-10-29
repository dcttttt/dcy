import  streamlit as st
import  pickle
import pickle
import streamlit as st


with open('rfc_model.pkl', 'rb') as f:
    rfc_model = pickle.load(f)


with open('output_uniques.pkl', 'rb') as f:
    output_uniques_map = pickle.load(f)

st.subheader('随机森林模型')
st.subheader('映射关系示例')

st.write(output_uniques_map[1])

