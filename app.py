import streamlit as st
string = "Largest Number Among 3"
st.set_page_config(page_title=string, page_icon="🔍")

st.title('Largest Number Finder')
x = st.number_input('Enter a number')
y = st.number_input('Enter a number')
z = st.number_input('Enter a number')

if x>y and x>z:
  st.write(x,"is the largest number")
elif y>x and y>z:
  st.write(y,"is the largest number")
elif z>x and z>y:
  st.write(z,"is the largest number")
else:
  st.write("The numbers are Equal")
