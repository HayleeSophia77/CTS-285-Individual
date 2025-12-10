# My prompts

These are the most useful prompts I used while building this project. They helped me understand session state, fix bugs, and make the UX better.

---

## Prompt 1: Session State for Auth

**What I asked:**

I've used Streamlit a few times but never built anything with authentication. How do I use `session_state` to keep track of whether someone is logged in across reruns? What's the best way to structure login and registration forms?

**Why it helped:**

This was my starting point. The response explained I needed to store `authenticated`, `current_user`, and `view` in session state, and that `st.form` would make validation cleaner. It basically set up the foundation for everything else.

**What I got from it:**

Session state is essential for anything that needs to persist across reruns. Without it, every button click resets everything.

---

## Prompt 2: Building the Whole System

**What I asked:**

Help me build a Citizen Wellness Portal Streamlit app with registration, login, a dashboard with metrics, and `session_state` for authentication.

**Why it helped:**

This gave me the overall structure — splitting things into functions like `init_session_state()`, `register_user()`, `check_credentials()`, `show_login_form()`, etc. It showed me how to organize code instead of having one giant messy file.

**What I got from it:**

Breaking functionality into separate functions makes debugging way easier. Each function does one thing and does it well.

---

## Prompt 3: Screen Switching Bug

**What I asked:**

My Streamlit app keeps losing which page I'm on when I click buttons.  
How do I use `st.session_state["view"]` to remember whether I'm on the login or registration screen?

**Why it helped:**

I was getting frustrated because the app randomly switched between login and registration. This prompt led me to use a `view` key in session state to explicitly track which screen to show.

**What I got from it:**

Don’t assume Streamlit will “remember” what screen you’re on. You have to explicitly track state and use it to decide what to render.

---

## Prompt 4: Double-Click Bug

**What I asked:**

When I click my login or logout buttons in Streamlit, I have to click twice before it actually changes pages. How can I fix this using `st.rerun()` or `st.experimental_rerun()`?

**Why it helped:**

This was the most annoying bug. The response explained that Streamlit decides what to show **before** the form logic runs, so I needed to call `st.rerun()` after changing auth state to force an immediate re-render.

**What I got from it:**

`st.rerun()` is crucial when you update important state and need the UI to reflect it immediately. Without it, changes don’t show until the next interaction.

---

## Prompt 5: Registration UX

**What I asked:**

After a successful registration, I want to show a countdown message and then automatically send the user back to the login page. How can I do that cleanly in Streamlit?

**Why it helped:**

This turned registration from “technically works but feels broken” into something polished. The response showed me how to use `st.empty()` as a placeholder and `time.sleep()` for the countdown.

**What I got from it:**

Small UX touches like countdown messages make a huge difference in how professional an app feels, even if the functionality is the same.

---

## What I Learned About Using AI

**What worked:**

- Asking specific questions about exact problems I was seeing  
- Describing the behavior I wanted vs what I was getting  
- Following up when the first solution didn’t work  

**What didn’t work:**

- Vague questions like “how do I make a login system” (too broad)  
- Asking without trying anything first  
- Copy-pasting code without understanding it  

**Bottom line:**

AI is super useful for getting unstuck on specific problems, but you still need to understand the code and be willing to debug when stuff breaks.