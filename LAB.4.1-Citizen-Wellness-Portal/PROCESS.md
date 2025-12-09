# Citizen Wellness Portal – PROCESS

## 1. What I Knew Before

- I've used Streamlit 2-3 times before this, so I wasn't completely new to it. 
- I've barely touched Flask, but just enough to know it exists and uses routing. 
- I definitely prefer Streamlit over Flask for how quick it is to get something working. That said, I hadn't built anything with authentication or session state management before, so that part was new.

## 2. LLM-Assisted Learning Prompts

### Phase 1 – Orientation

**Prompt:**

"I've used Streamlit a few times but never built anything with authentication. How do I use session_state to keep track of whether someone is logged in across reruns? What's the best way to structure login and registration forms?"

**What I learned (summary):**

Session state is key for authentication since Streamlit reruns everything. I needed to store stuff like authenticated, current_user, and which screen we're on (view). The approach is to check session state at the start of each rerun to decide what to show. Forms can use st.form to batch inputs together, which makes validation cleaner.

---

### Phase 2 – Core Feature Implementation

**Prompt:**

"Help me build a Citizen Wellness Portal Streamlit app with registration, login, a dashboard with metrics, and session_state for authentication."

**What I changed in my code:**

- Set up a users dict in st.session_state to store credentials
- Created session state keys for authenticated, current_user, metrics, and view
- Split everything into functions so it's not just one giant mess:

- init_session_state()
- register_user()
- check_credentials()
- show_registration_form()
- show_login_form()
- show_dashboard()
- logout()

* Got the dashboard working with those 4 "Algorithmic Satisfaction Metrics" with progress bars and a status message

---

### Phase 3 – Debugging Session State

**Prompt:**

"My Streamlit app keeps losing which page I'm on when I click buttons. How do I use st.session_state to remember whether I'm on the login or registration screen?"

**The fix:**

So I made an init_session_state() function that sets up all the default keys once. Then I used st.session_state to track whether we're showing login or registration. The Login/Register buttons just update that view state instead of trying to show both screens at the same time. Way cleaner.

---

### Phase 4 – Refinement & UX

**Prompt:**

"When I click my login or logout buttons in Streamlit, I have to click twice before it actually changes pages. How can I fix this using st.rerun() or st.experimental_rerun()?"

**What I learned:**

The problem was that Streamlit figures out what screen to show BEFORE the form's submit logic even runs. So I had to call st.rerun() right after changing important session state stuff. Updated show_login_form() and logout() to both use st.rerun() after they change the authentication state. That fixed the annoying double-click thing.

**Prompt (UX refinement):**

"After a successful registration, I want to show a countdown message and then automatically send the user back to the login page. How can I do that cleanly in Streamlit?"

**What I built:**

Added a placeholder at the top of the registration screen for messages. After someone registers successfully, it shows a success message, then counts down from 3 with "Redirecting to login in X seconds..." before switching them to the login screen. Makes it feel way more polished than just dumping them back on the registration page.

---

## 3. Challenges and How I Resolved Them

1. Managing authentication state properly

- Even though I'd used Streamlit before, I hadn't dealt with login/logout flows
- Had to think through what needed to persist (authenticated status, username, which screen to show)
- Learned to initialize everything in one place with init_session_state() to avoid key errors

2. Keeping track of which screen to show

- The app kept flipping between login and registration at random
- Fixed it by adding st.session_state and actually using it consistently in main() to control which form renders

3. Everything needed two clicks to work

- First click would show success messages but wouldn't actually change the screen until you clicked something else
- Turned out I needed to use st.rerun() right after updating authentication stuff so it immediately re-renders with the new state

4. Registration UX was confusing

- Just staying on the registration page after success was technically fine but felt broken
- Added the countdown redirect thing which makes it way more obvious what's happening

---

## 4. Flask vs Streamlit – My Take on Both

Streamlit:

- Single Python script that reruns on interactions
- UI built directly in Python, no HTML needed
- State managed through st.session_state
- Super fast for dashboards and internal tools
- What I prefer working with

Flask:

- Route-based with @app.route decorators
- Uses HTML templates (Jinja)
- More traditional web framework approach
- Haven't used it much

What surprised me about this project:

- How much session state management matters for auth flows—more complex than my previous Streamlit projects
- How easy it was to make something that looks decent without touching HTML/CSS
- The st.rerun() trick for fixing the double-click bug—that wasn't obvious at first
- That I could build this whole login/registration/dashboard system pretty quickly once I figured out the session state patterns
