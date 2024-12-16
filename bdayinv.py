import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image
import base64
st.set_page_config(page_title="CWUBILPNKG", page_icon=":tada:", layout="wide")

def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.

    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "gif"
        
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )

def load_ani(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.balloons()
st.title("Happy Birthday!")
set_bg_hack("gojo.gif")
local_css("style/style.css")
fire = load_ani("https://lottie.host/b04355b3-8474-4538-9422-536e4775b8c1/kEfzCeYZZS.json")
cwu = Image.open('cwu.jpg')
drizzy = Image.open('drizzy.jpg')
bday = load_ani("https://lottie.host/1c6590ca-da87-498e-98b5-273f5063a066/DbzPs2ALwj.json")
kitty = load_ani("https://lottie.host/95e1252c-7e3f-46e2-b275-7084368aa797/V8j0QWhRgp.json")
jem = load_ani("https://lottie.host/c72b966f-0321-44fb-bb5b-fd958f952b32/RS50KdB79Q.json")
#-- Password ---
# Website Content:

# ---Header---
st.header("Fatih's BDAY Bash")
left_column, right_column = st.columns(2)
with left_column:
    st.image(cwu, width=900)
    st.title("Fatih's Invitation")
with right_column:
    st_lottie(bday, height=400, key="birth")
# -- Info --
with st.container():
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write("---")
        st.header("Information >:)")
        st.title("Date:")
        st.write(" Fatih's Birthday, 2024 at 6pm")
        st_lottie(fire, height=450,key="fiyah")
        st.title("Itinerary:")
        st.write("""
            - Chillaxing
            - perhaps some zaza
            - More Chillaxing
            - Hanging out
            - Have pizza
            - Porto's Cheesecake
            - Music
            - Poggers
            - 1V1 SUPER SMASH BROS ULTIMATE TOURNAMENT
                - Winner gets a prize!!!!
            - Maybe even a lil boba trip who knows
            - Go where the night takes us
            - Enjoy ourselves
            - Have fun hehehehe
            """)
        st_lottie(kitty, width=400, key="cat")
    with right_column:
        st.image(drizzy,width=500)
        st_lottie(jem, key="jemjem")