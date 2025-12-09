# SELF-ASSESSMENT – Citizen Wellness Portal™

## Functional Application

- [x] Citizens can register with validation (non-empty username, unique username, minimum password length).
- [x] Citizens can log in with correct credentials.
- [x] Dashboard only shows when authenticated and displays the citizen's username and four metrics.
- [x] Logout clears authentication state and returns the user to the login screen.

**Notes:**  
I tested multiple edge cases:
- Empty username, short password, and duplicate usernames all show appropriate error messages.
- Invalid login attempts show an error and do not reveal the dashboard.
- Successful registration now shows a brief redirect message and then sends the user back to the login page.

---

## Learning Demonstration

- Used LLMs (ChatGPT / Claude) to:
  - Understand Streamlit's rerun model and `st.session_state`.
  - Implement registration and login flows with persistent state.
  - Design the dashboard layout and status logic.
  - Fix the “double-click needed” issue for login/logout and improve the post-registration UX.
- Documented prompts, iterations, and decisions in `PROCESS.md`.

**Notes:**  
I treated the assignment as practice in learning a new framework using AI assistance. I asked specific questions when I got stuck (state, reruns, redirects) and then implemented and tested the suggested solutions.

---

## Code Quality

- Organized helper functions (`init_session_state`, `register_user`, `check_credentials`, `show_registration_form`, `show_login_form`, `show_dashboard`, `logout`).
- Centralized state initialization and authentication logic.
- Basic error handling and user feedback using Streamlit's `st.error`, `st.success`, and `st.info`.
- Comments explain key ideas such as:
  - Why `st.session_state` is used.
  - How metrics are generated.
  - How the redirect after registration works.

**Notes:**  
The code is structured so that core logic (auth, metrics) is separated from presentation (forms and dashboard). This should make it easier to extend later if needed.

---

## Git Workflow

- [ ] Created issue before development.
- [ ] Used a feature branch.
- [ ] Made atomic commits.
- [ ] Opened a pull request.

**Notes:**  

- If you complete the full workflow, update the checkboxes to `[x]` and briefly mention:
  - Issue number.
  - Branch name.
  - That you opened a PR summarizing the work.
- If you do **not** use the full workflow for this assignment, leave them unchecked and you can add a short note such as:
  - "For this assignment I focused mainly on the application and documentation; Git workflow steps were not fully executed but I understand the expected process."
