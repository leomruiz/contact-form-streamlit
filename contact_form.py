import streamlit as st  # pip install streamlit

left_column, center_column, right_column = st.columns([1,2,1])

with left_column:
    
    geo = ["GeoH2.jpg"]
    
    st.image(geo,width=150)

with center_column:

    st.markdown("<h1 style='text-align: center; color: blue;'> Get In Touch With Us! </h1>", unsafe_allow_html=True)
    
with right_column:
    
    starr = ["Starr_logo_280.png"]
    
    st.image(starr,width=500)




contact_form = """
<form action="https://formsubmit.co/YOUREMAIL@EMAIL.COM" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

with st.container():
    
    st.write("---")
    
    left_column, center_column, right_column = st.columns([1,2,1])

    with left_column:


        st.markdown(contact_form, unsafe_allow_html=True)

st.markdown(contact_form, unsafe_allow_html=True)

# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
