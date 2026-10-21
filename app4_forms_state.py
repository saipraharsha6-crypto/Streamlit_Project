import streamlit as st

st.title("Forms + Session State")

# --- Counter using session_state ---
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write("Counter:", st.session_state.count)

# --- Form ---
with st.form("login_form"):
    st.subheader("Login")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    submit = st.form_submit_button("Login")

if submit:
    if user == "admin" and pwd == "1234":
        st.session_state.logged_in = True
        st.success("Login successful!")
    else:
        st.error("Invalid credentials")

if st.session_state.get("logged_in"):
    st.info("Welcome, admin! You are now logged in.")