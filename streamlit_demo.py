import streamlit as st

f_num = st.number_input("Insert first number", value=None, placeholder="Type a number...")

s_num = st.number_input("Insert second number", value=None, placeholder="Type a number...")


choice = st.radio(
        "Please select one of the arithmetic operators ",
        ["Addition", "Subtraction", "Multiplication","Division"],
        index = None
        )

if choice == "Addition" :
    result = f_num + s_num
    st.write("Answer is ",result)
    
elif choice == "Subtraction" :
    result = f_num - s_num
    st.write("Answer is ",result)
    
elif choice == "Multiplication" :
    result = f_num * s_num
    st.write("Answer is ",result)
    
else :
    result = f_num / s_num
    st.write("Answer is ",result)
   
