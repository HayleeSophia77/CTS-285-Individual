# SELF-ASSESSMENT – Citizen Wellness Portal

## Functional Application

- [X] Citizens can register with validation (non-empty username, unique username, minimum password length).
- [X] Citizens can log in with correct credentials.
- [X] Dashboard only shows when authenticated and displays the citizen's username and four metrics.
- [X] Logout clears authentication state and returns the user to the login screen.

**Notes:**  

I tested a bunch of edge cases to make sure everything works:
- Empty usernames -> Shows error
- Short passwords -> Shows error
- Duplicate usernames -> Shows error
- Wrong credentials on login -> Shows error, no dashboard access
- Registration -> Shows countdown redirect before switching to login

---

## Learning Demonstration

Used ChatGPT and Claude to figure out the authentication and session state parts since I hadn't built that before:  
- How to manage auth state with st.session_state for login/logout flows
- Designing the dashboard layout and status logic
- Fixing that annoying double-click bug with st.rerun()
- Making the registration redirect feel smoother

**Notes:**  
Used AI to help figure out the session state patterns for auth instead of just guessing. Actually implemented and tested everything myself rather than copy-pasting. I had to debug a bunch of stuff that didn't work the first time.

---

## Code Quality

**Organization:**

	Split everything into helper functions:

		- init_session_state() - Initialize all session keys
		- register_user() - Handle user registration
		- check_credentials() - Validate login
		- show_registration_form() - Display registration UI
		- show_login_form() - Display login UI
		- show_dashboard() - Display authenticated dashboard
		- logout() - Clear session and return to login

**Error Handling:**

- Added error handling and user feedback with Streamlit's message functions
- Validation for usernames and passwords
- Clear error messages for all failure cases

**Documentation:**

	- Commented the important parts:

		- Why st.session_state is needed
		- How the metrics get generated
		- How the registration redirect works

**Notes:**  
Organized it so the core logic(auth, metrics) is separate from the UI stuff(forms and dashboard). Should make it easier to add features later if I need to.

---

## Git Workflow

- [X] Created issue before development.
- [X] Used a feature branch.
- [X] Made atomic commits.
- [X] Opened a pull request.

**Notes:**  

Completed full Git workflow including issue creation, feature branch, atomic commits, and pull request documentation.

---

## AI Assistance Documentation

**Tools Used:**

ChatGPT & Claude

- Initial authentication structure and session state patterns
- Bug fixes, and UX improvements

**What AI Helped With:**

- Session state management patterns for authentication
- Form validation structure
- Fixing the double-click bug with st.rerun()
- Creating the countdown redirect UX

**What I Did Myself:**

- All implementation and testing
- Debugging when stuff broke
- Deciding how to structure functions and organize the code
- Testing edge cases (empty usernames, duplicate users, wrong passwords, etc.)
