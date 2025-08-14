import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000/api/"

# Helper function to change pages and force rerun
def go_to_page(page_name):
    st.session_state.page = page_name
    st.session_state._page_changed = not st.session_state.get("_page_changed", False)

# Initialize session state variables
if "token" not in st.session_state:
    st.session_state.token = None
if "username" not in st.session_state:
    st.session_state.username = None


def register_user():
    st.title("📝 Register")

    # Use session state to track registration success
    if "registration_success" not in st.session_state:
        st.session_state.registration_success = False

    with st.form("register_form"):
        full_name = st.text_input("Full Name")
        mobile_number = st.text_input("Mobile Number")
        address = st.text_area("Address")
        email = st.text_input("Email")
        location = st.selectbox("Location", ["Hyderabad", "Bangalore", "Mumbai"])
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        submitted = st.form_submit_button("Register")

        if submitted:
            payload = {
                "username": email.split("@")[0],
                "password": password,
                "confirm_password": confirm_password,
                "email": email,
                "full_name": full_name,
                "mobile_number": mobile_number,
                "address": address,
                "location": location
            }

            try:
                res = requests.post(BASE_URL + "register/", json=payload)
                if res.status_code == 201:
                    st.success("Registration successful! Please log in below.")
                    st.session_state.registration_success = True
                else:
                    st.error(res.json())
            except Exception as e:
                st.error(f"Error: {e}")

    # Show button after successful registration
    if st.session_state.registration_success:
        if st.button("Go to Login"):
            st.session_state.registration_success = False
            go_to_page("login")

    # Always show a button to go to login (for users who want to switch)
    if st.button("Already have an account? Login here"):
        st.session_state.registration_success = False
        go_to_page("login")


def login_user():
    st.title("🔑 Login")

    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            payload = {
                "username": email.split("@")[0],
                "password": password
            }

            try:
                res = requests.post(BASE_URL + "login/", json=payload)
                if res.status_code == 200:
                    data = res.json()
                    st.session_state.token = data["token"]
                    st.session_state.username = data["username"]
                    st.success("Login successful!")
                    go_to_page("home")
                else:
                    st.error("Invalid credentials")
            except Exception as e:
                st.error(f"Error: {e}")

    # Button to go to registration for new users
    if st.button("Don't have an account? Register here"):
        go_to_page("register")


def home_page():
    st.title(f"Welcome, {st.session_state.username}! 🎉")
    if st.button("Logout"):
        try:
            headers = {"Authorization": f"Token {st.session_state.token}"}
            res = requests.post(BASE_URL + "logout/", headers=headers)
            if res.status_code == 200:
                st.success("Logged out successfully")
                st.session_state.token = None
                go_to_page("login")
            else:
                st.error("Logout failed")
        except Exception as e:
            st.error(f"Error: {e}")


# Page Navigation
if "page" not in st.session_state:
    st.session_state.page = "login"  # Default page is login

if st.session_state.page == "register":
    register_user()
elif st.session_state.page == "login":
    login_user()
elif st.session_state.page == "home":
    home_page()
