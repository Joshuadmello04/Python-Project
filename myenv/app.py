import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
import pickle
from pathlib import Path
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# ---- USER AUTH ----
with open("config.yaml") as file:
    config = yaml.safe_load(file)


authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    config["preauthorized"],
)

name, authentication_status, username = authenticator.login()

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.title(f"Welcome *{name}*")
    page = st.sidebar.selectbox("Explore Or Predict", ("Predict", "Explore"))

    if page == "Predict":
        show_predict_page()
    else:
        show_explore_page()

elif authentication_status == False:
    st.error("Username/password is incorrect")
elif authentication_status == None:
    st.warning("Please enter your username and password")
