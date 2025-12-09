# LAB.4.1
# 12/08/2025
# Haylee Paredes

import streamlit as st
import random
import time

# ═══════════════════════════════════════════════════════════════════════
#  CITIZEN WELLNESS PORTAL™
#  AlgoCratic Futures - ORANGE Clearance Authorization
# ═══════════════════════════════════════════════════════════════════════
#
#  Your mission: Build a login/registration system with dashboard
#  using Streamlit and AI-assisted learning.
#
#  This file is a COMPLETE EXAMPLE IMPLEMENTATION that satisfies the
#  assignment requirements. Read through it and adapt / simplify as
#  needed so you fully understand every part.
#
#  Run with: streamlit run app.py
# ═══════════════════════════════════════════════════════════════════════


# ----- Helpers to initialize session state --------------------------------

def init_session_state() -> None:

    if "users" not in st.session_state:
        # In-memory user store: {"username": "password"}
        st.session_state["users"] = {}

    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if "current_user" not in st.session_state:
        st.session_state["current_user"] = None

    if "metrics" not in st.session_state:
        st.session_state["metrics"] = None

    if "view" not in st.session_state:
        # "login" or "register"
        st.session_state["view"] = "login"

# ----- Core auth functions -------------------------------------------------

def register_user(username: str, password: str) -> tuple[bool, str]:
    """
    Returns:
        success: bool
        message: str
    """
    username = username.strip()

    if not username:
        return False, "Username cannot be empty."

    if len(password) < 4:
        return False, "Password must be at least 4 characters."

    users = st.session_state["users"]

    if username in users:
        return False, "Username already taken. Please choose another."

    users[username] = password
    # store back for clarity
    st.session_state["users"] = users

    return True, "Registration successful! You may now log in."


def check_credentials(username: str, password: str) -> bool:

    users = st.session_state.get("users", {})
    return username in users and users[username] == password

# ----- UI sections ---------------------------------------------------------

def show_registration_form() -> None:

    st.subheader("Citizen Registration")

    top_message_placeholder = st.empty()

    with st.form("registration_form"):
        username = st.text_input("Desired Username")
        password = st.text_input("Choose a Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submitted = st.form_submit_button("Register with The Algorithm")

    if submitted:
        if password != confirm_password:
            top_message_placeholder.error("Passwords do not match.")
            return

        success, message = register_user(username, password)
        if success:
            # All messages now appear at the TOP in this placeholder
            with top_message_placeholder.container():
                st.success(message)
                countdown_placeholder = st.empty()
                for i in range(3, 0, -1):
                    countdown_placeholder.info(
                        f"Redirecting you to the login portal in {i} seconds..."
                    )
                    time.sleep(1)

            st.session_state["view"] = "login"
            # or st.experimental_rerun() if needed
            st.rerun()
        else:
            top_message_placeholder.error(message)

def show_login_form() -> None:

    st.subheader("Citizen Login")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Submit to The Algorithm")

    if submitted:
        if check_credentials(username, password):
            st.session_state["authenticated"] = True
            st.session_state["current_user"] = username
            # Generate metrics once per login
            st.session_state["metrics"] = generate_metrics()
            st.success(f"Access granted. Welcome, Citizen {username}.")
            # immediately rerun so main() sees authenticated == True
            st.rerun()  
        else:
            st.error("Invalid credentials. The Algorithm does not recognize this citizen.")


def generate_metrics() -> dict:

    # You can make these static if you prefer; random is allowed by the spec.
    return {
        "Productivity Score": random.randint(60, 95),
        "Compliance Rating": random.randint(80, 100),
        "Happiness Index": random.randint(50, 90),
        "Loyalty Quotient": random.randint(70, 100),
    }


def show_dashboard() -> None:

    username = st.session_state.get("current_user", "Unknown")

    st.header(f"Welcome, Citizen {username}!")
    st.write("---")
    st.subheader("YOUR ALGORITHMIC SATISFACTION METRICS™")

    metrics = st.session_state.get("metrics") or generate_metrics()
    st.session_state["metrics"] = metrics

    # Nicely formatted metrics with progress bars
    for label, value in metrics.items():
        st.write(f"**{label}:** {value}%")
        st.progress(value)

    st.write("---")

    # Simple status message based on metrics
    avg_score = sum(metrics.values()) / len(metrics)
    if avg_score >= 80:
        status = "WITHIN ACCEPTABLE PARAMETERS"
    elif avg_score >= 60:
        status = "MONITORING RECOMMENDED"
        # you can change wording to match assignment vibe if you want
    else:
        status = "ALERT: CITIZEN REQUIRES INTERVENTION"

    st.success(f"Status: {status}")

    if st.button("Logout"):
        logout()

def logout() -> None:

    st.session_state["authenticated"] = False
    st.session_state["current_user"] = None
    st.session_state["metrics"] = None
    st.session_state["view"] = "login"
    st.info("You have been safely logged out of the Portal.")
    # rerun so main() sees authenticated == False and shows login
    st.rerun()

# ----- Main app ------------------------------------------------------------

def main():
    
    init_session_state()

    st.set_page_config(
        page_title="Citizen Wellness Portal™",
        page_icon="🛰️",
        layout="centered",
    )

    st.title("Citizen Wellness Portal™")
    st.caption("AlgoCratic Futures • Internal Use Only • ORANGE Clearance")

    if not st.session_state["authenticated"]:
        # Navigation for unauthenticated citizens: Login vs Register
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Login", use_container_width=True):
                st.session_state["view"] = "login"
        with col2:
            if st.button("Register", use_container_width=True):
                st.session_state["view"] = "register"

        st.write("---")

        if st.session_state["view"] == "login":
            show_login_form()
        else:
            show_registration_form()
    else:
        # Authenticated: show dashboard only
        show_dashboard()


if __name__ == "__main__":
    main()