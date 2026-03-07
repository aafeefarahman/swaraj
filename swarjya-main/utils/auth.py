import os
import requests
import firebase_admin
from firebase_admin import credentials, auth
from firebase_admin.exceptions import FirebaseError
import streamlit as st

# ------------------- CONFIG ------------------- #

# Path to your Firebase service account JSON
SERVICE_ACCOUNT_PATH = os.path.join(
    "secrets", "swarjya-translator-firebase-adminsdk-fbsvc-f10366303b.json"
)

# Web API key (from Firebase Console → Project Settings → General → Web API Key)
FIREBASE_WEB_API_KEY = os.getenv("FIREBASE_WEB_API_KEY")

# Initialize Firebase Admin SDK (for secure server-side actions)
if not firebase_admin._apps:
    cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred)

# ------------------- AUTH HELPERS ------------------- #

def signup(email, password):
    """Create a new user in Firebase Authentication (Admin SDK)."""
    try:
        user = auth.create_user(email=email, password=password)
        st.success("Signup successful! Please login.")
        return True
    except FirebaseError as e:
        st.error(f"Signup failed: {e}")
        return False


def login(email, password):
    """Login with email & password using Firebase REST API."""
    try:
        if not FIREBASE_WEB_API_KEY:
            st.error("Missing FIREBASE_WEB_API_KEY in environment.")
            return False

        url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_WEB_API_KEY}"
        payload = {"email": email, "password": password, "returnSecureToken": True}

        res = requests.post(url, json=payload)
        data = res.json()

        if "error" in data:
            st.error(f"Login failed: {data['error']['message']}")
            return False

        # Save user session in Streamlit
        st.session_state.user = data
        st.session_state.email = email
        st.success("Login successful!")
        return True

    except Exception as e:
        st.error(f"Login failed: {e}")
        return False


def logout():
    """Clears session state."""
    st.session_state.user = None
    st.session_state.email = None
    st.success("Logged out!")


def is_authenticated():
    """Check if user is logged in."""
    return st.session_state.get("user") is not None


def get_user_email():
    """Return current user's email."""
    return st.session_state.get("email", "Guest")


def reset_password(email):
    """Send password reset email using Firebase REST API."""
    try:
        if not FIREBASE_WEB_API_KEY:
            st.error("Missing FIREBASE_WEB_API_KEY in environment.")
            return False

        url = f"https://identitytoolkit.googleapis.com/v1/accounts:sendOobCode?key={FIREBASE_WEB_API_KEY}"
        payload = {"requestType": "PASSWORD_RESET", "email": email}

        res = requests.post(url, json=payload)
        data = res.json()

        if "error" in data:
            st.error(f"Reset failed: {data['error']['message']}")
            return False

        st.success(f"Password reset email sent to {email}.")
        return True

    except Exception as e:
        st.error(f"Password reset failed: {e}")
        return False
