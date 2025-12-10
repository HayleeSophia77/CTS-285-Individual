# Citizen Wellness Portal

A Streamlit-based web app where citizens can register, log in, and view their Algorithmic Satisfaction Metrics.  
Built for CTS-285 final assessment to show I can make a working web app using Streamlit and AI assistance.

---

## What It Does:

### User Registration

- Checks username isn't empty or already taken
- Password has to be at least 4 characters
- Shows a success message + countdown before redirecting to login

### Login System

- Verifies your credentials
- Keeps you logged in using `st.session_state`
- Shows error messages if username/password is wrong

### Citizen Dashboard

Once you're logged in, you see your Algorithmic Satisfaction Metrics with progress bars:
- Productivity Score
- Compliance Rating
- Happiness Index
- Loyalty Quotient

Plus a status message based on your average score:
- within acceptable parameters
- monitoring recommended
- citizen requires intervention

### Logout

- Clears your session and sends you back to login instantly (using `st.rerun()`)

### Other Stuff

- Registration redirect has a countdown so you know what's happening
- Fixed the annoying double-click bug with `st.rerun()`
- Clean UI built with Streamlit components

---

## Running It

### What You Need
- Python 3.7 or newer
- pip

### Setup

1. **Get the files**
   ```bash
   git clone https://github.com/HayleeSophia77/CTS-285-Individual.git
   cd CTS-285-Individual/LAB.4.1-Citizen-Wellness-Portal