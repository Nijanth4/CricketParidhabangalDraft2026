import streamlit as st
import sqlite3
import hashlib

DB_PATH = "users.db"


# -------------------- DATABASE --------------------

def create_users_table():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT
        )
    """)
    conn.commit()
    conn.close()


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    try:
        c.execute(
            "INSERT INTO users (username, password_hash) VALUES (?, ?)",
            (username, hash_password(password))
        )
        conn.commit()
        success = True
    except sqlite3.IntegrityError:
        success = False

    conn.close()
    return success


def authenticate_user(username, password):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute(
        "SELECT password_hash FROM users WHERE username = ?",
        (username,)
    )
    row = c.fetchone()
    conn.close()

    if not row:
        return False

    return row[0] == hash_password(password)


# -------------------- STREAMLIT UI --------------------

def login():
    create_users_table()

    st.subheader("🏏 Fantasy Cricket Login")

    tab_login, tab_register = st.tabs(["Login", "Register"])

    # ---------------- LOGIN TAB ----------------
    with tab_login:
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):
            if authenticate_user(username, password):
                st.session_state["user"] = username
                st.success(f"Welcome back, {username}!")
                st.rerun()
            else:
                st.error("Invalid username or password")

    # ---------------- REGISTER TAB ----------------
    with tab_register:
        new_user = st.text_input("Choose Username", key="reg_user")
        new_pass = st.text_input("Choose Password", type="password", key="reg_pass")
        confirm_pass = st.text_input("Confirm Password", type="password")

        if st.button("Register"):
            if not new_user or not new_pass:
                st.error("Username and password required")
            elif new_pass != confirm_pass:
                st.error("Passwords do not match")
            else:
                if register_user(new_user, new_pass):
                    st.success("Registration successful! Please login.")
                else:
                    st.error("Username already exists")
``
