import pickle
from pathlib import Path 

import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher

names = ["Vivian Ludrick", "Joshua Dmello"]
usernames = ["vivalchemy", "jdmello"]
passwords = ["87654321", "12345678"] 

hashed_passwords = Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

