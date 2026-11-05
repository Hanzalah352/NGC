import base64
from PIL import Image
import streamlit as st
from pypdf import PdfReader
import pandas as pd


# 1. Page Definition Function
def home_page():
    # Main Page Header
    st.markdown("<h1 style='color: black; margin-top: 0px;'>Welcome to the NGC</h1>", unsafe_allow_html=True)
    # write this paragraph in the center of the page with a font size of 23px and color black : The National Transmission and Despatch Company (NTDC) operates Pakistan's largest interconnected power grid, linking generation plants to regional distribution networks nationwide. Established in 1998 and headquartered in Lahore, we manage the bulk transmission, engineering, and economic dispatch of electricity across the country. Today, we are modernizing our network with next-generation EHV technologies and cross-border power connections to deliver safer, more reliable energy infrastructure for Pakistan's future.
    st.markdown(
        "<p style='text-align: center; font-size: 23px; color: black;'>    The National Transmission and Despatch Company (NTDC) operates Pakistan's largest interconnected power grid, linking generation plants to    regional distribution networks nationwide. Established in 1998 and headquartered in Lahore, we manage the bulk transmission, engineering, and economic dispatch of electricity across the country. Today, we are modernizing our network with next-generation EHV technologies and cross-border power connections to deliver safer, more reliable energy infrastructure for Pakistan's future.</p>", 
        unsafe_allow_html=True
    )
    
    # Creates space between the header and the profile grid
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
   

    

    # 3-Column Leadership Layout Grid
    col1, col2, col3 = st.columns(3)

    # Left Profile: Federal Secretary
    with col1:
        st.image("f.jpeg", use_container_width=True)
        st.markdown(
            """
            <div style='text-align: center;'>
                <p style='margin-bottom: 2px; font-size: 14px; color: #202020;'>Federal Secretary (Power Division)</p>
                <strong style='font-size: 16px; color: black;'>Dr. Muhammad Fakhre Alam Irfan</strong>
            </div>
            """, 
            unsafe_allow_html=True
        )

    # Middle Profile: Federal Minister
    with col2:
        st.image("aw.jpg", use_container_width=True)
        st.markdown(
            """
            <div style='text-align: center;'>
                <p style='margin-bottom: 2px; font-size: 14px; color: #202020;'>Federal Minister<br>for Energy (Power Division)</p>
                <strong style='font-size: 16px; color: black;'>Sardar Awais Ahmad Khan Leghari</strong>
            </div>
            """, 
            unsafe_allow_html=True
        )

    # Right Profile: Managing Director
    with col3:
        st.image("Altaf_Hussain.jpg", use_container_width=True)
        st.markdown(
            """
            <div style='text-align: center;'>
                <p style='margin-bottom: 2px; font-size: 14px; color: #202020;'>Managing Director NTDC</p>
                <strong style='font-size: 16px; color: black;'>Engr. Altaf Hussain Malik</strong>
            </div>
            """, 
            unsafe_allow_html=True
        )
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.subheader("Our Services")
    st.image("ser.png", use_container_width=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.subheader('Energy Resources')
    st.image("imag.png", use_container_width=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.subheader('Transmission Networks')
    st.image("tran.png", use_container_width=True)
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.title('Our Projects and Plans')
    st.image("proc.png", use_container_width=True)
    if st.button('View More'):
        st.switch_page(projects)
def about():
    st.title("Our Projects and Plans")
    # writes this paragraph in the center of the page with a font size of 23px and color black
    try:
        reader = PdfReader("ng.pdf")
        pdf_text = ""
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pdf_text += text + "\n"
        
        # Display the extracted paragraph centered, 23px font size, and black color
        st.markdown(
            f"""
            <div style='text-align: center; font-size: 23px; color: black; line-height: 1.5; max-width: 900px; margin: 0 auto;'>
                {pdf_text}
            </div>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.markdown(
            "<div style='text-align: center; color: red;'>ng.pdf file not found.</div>", 
            unsafe_allow_html=True
        )
def investments():
    st.title('Our Investments')
    df = pd.read_csv("ne.csv")
    st.dataframe(df, use_container_width=True)

# 2. Application Entry Initialization (Must be first Streamlit commands execution)
try:
    logo_image = Image.open("logo.jfif")
except FileNotFoundError:
    logo_image = "🧭"  # Fallback icon layout placeholder

st.set_page_config(
    page_title="NGC",
    page_icon=logo_image,
    layout="wide"
)

def projects():
    st.title('Our Projects')
    # put file named pro.csv as a table in the page
    df = pd.read_csv("pro.csv")
    st.dataframe(df, use_container_width=True)




# 3. Dynamic Base64 Background Injector Function
def set_background(image_file):
    try:
        with open(image_file, "rb") as f:
            img_data = f.read()
        b64_encoded = base64.b64encode(img_data).decode()
        style = f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{b64_encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
        """
        st.markdown(style, unsafe_allow_html=True)
    except FileNotFoundError:
        pass  # Fallback gracefully if scenery picture is missing

# Render layout scenery layer background
set_background("line.jpg")


# 4. Streamlit Navigation Frame Router Setup
home = st.Page(home_page, title="Home", default=True)
about = st.Page(about, title="About")
investments = st.Page(investments, title="Investments")
projects = st.Page(projects, title="Projects")
# Build and execute the structural modern app framework engine put it like navigation bar at the top of the page with a horizontal orientation and tabs style
pg = st.navigation([home, about, investments, projects], position="top")

pg.run()
