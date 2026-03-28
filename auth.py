import streamlit as st

def login():
    st.subheader("Login with IPL Fantasy Account")

    username = st.text_input("IPL Username")
    password = st.text_input("IPL Password", type="password")

    if st.button("Login"):
        # ❌ IPL does NOT expose auth APIs
        # ✅ Replace this with official OAuth / SSO token validation when licensed
        if username and password:
            st.session_state["user"] = username
            st.success("Login Successful")
        else:
            st.error("Invalid credentials")