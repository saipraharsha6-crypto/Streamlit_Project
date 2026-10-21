import streamlit as st
from db import init_db, create_user, get_user_by_username
from auth import (
    hash_password,
    verify_password,
    validate_username,
    validate_email,
    validate_password
)

st.set_page_config(
    page_title="Login & Signup",
    page_icon="🔐"
)

init_db()


def login_page():
    st.title("🔐 Login")

    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")
    if st.button("Login", key="login_button"):
        user = get_user_by_username(username)

        if user and verify_password(password, user["password_hash"]):
            st.session_state.logged_in = True
            st.session_state.username = user["username"]
            st.session_state.user = user
            st.rerun()
        else:
            st.error("Invalid username or password.")


def signup_page():
    st.title("📝 Create Account")

    username = st.text_input("Username", key="signup_username")
    email = st.text_input("Email", key="signup_email")
    password = st.text_input(
        "Password",
       type="password",
       key="signup_password"
)
    confirm_password = st.text_input(
       "Confirm Password",
       type="password",
        key="signup_confirm_password"
)
    

    if st.button("Sign Up", key="signup_button"):
        valid, message = validate_username(username)

        if not valid:
            st.error(message)
            return

        valid, message = validate_email(email)

        if not valid:
            st.error(message)
            return

        valid, message = validate_password(password)

        if not valid:
            st.error(message)
            return

        if password != confirm_password:
            st.error("Passwords do not match.")
            return

        if get_user_by_username(username):
            st.error("Username already exists.")
            return

        password_hash = hash_password(password)

        create_user(
            username,
            email,
            password_hash
        )

        st.success("Account created successfully! Please login.")


def dashboard_page():
    st.title("🎉 Welcome!")

    user = st.session_state.user

    st.write(f"Welcome, **{user['username']}**!")

    st.subheader("Your Account")

    st.write(f"**User ID:** {user['id']}")
    st.write(f"**Username:** {user['username']}")
    st.write(f"**Email:** {user['email']}")
    st.write(f"**Joined:** {user['created_at']}")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.pop("username", None)
        st.session_state.pop("user", None)
        st.rerun()


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if st.session_state.logged_in:
    dashboard_page()

else:
    tab1, tab2 = st.tabs(["Login", "Sign Up"])

    with tab1:
        login_page()

    with tab2:
        signup_page()