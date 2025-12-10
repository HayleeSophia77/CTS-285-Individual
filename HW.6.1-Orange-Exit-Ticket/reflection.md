# My reflection

## What I Built

An authentication system in Streamlit with user registration, login, and a dashboard. Users can make accounts, log in, see their fake "wellness metrics," and log out. Everything uses session state so it persists when Streamlit reruns the script.

---

## What Worked:

### Session state management

Once I got the pattern down, I initialized everything in `init_session_state()` and store `authenticated`, `current_user`, `metrics`, and `view` in session state, managing auth became straightforward. Just had to remember to check session state at the start of each rerun.

### Using `st.rerun()`

This fixed the annoying double-click bug. After updating auth state, calling `st.rerun()` makes the app immediately re-render with the new state. Simple fix but made a huge difference.

### AI for debugging

When I got stuck on specific bugs (screen switching, double-click issue), asking ChatGPT/Claude with details about what I was seeing got me unstuck fast. Way better than just asking "how do I build a login system."

### Countdown redirect

Adding the "Redirecting to login in 3...2...1..." message after registration made it feel way more polished. Users actually know what's happening instead of wondering why they're still on the registration page.

---

## What Didn't Work/What I'd Change:

### In-memory storage

Using a dict in session state means all users disappear when the app restarts. For anything real I'd need an actual database. SQLite at minimum, probably PostgreSQL for production.

### No password hashing

Storing passwords as plain text is terrible. Should be using bcrypt or argon2 to hash them before storing.

### Validation is basic

Just checking for empty usernames and passwords over 4 characters. Real apps need way more: email validation, password strength requirements, username character restrictions, etc.

### No password recovery

If you forget your login, you're just locked out. Would need email verification and a reset flow for a real app.

### Metrics don't mean anything

The dashboard just shows random numbers. For a real wellness portal these would need to track actual data.

---

## What I Learned:

### Session state is crucial for Streamlit auth

Even though I'd used Streamlit before, building an auth system really showed me how important session state is. Every interaction reruns the entire script, so anything that needs to stick around has to live in `st.session_state`.

### `st.rerun()` matters for state changes

When you update important state like authentication status, you need to force an immediate rerun or the UI won't update until the next button click. Wasn't obvious at first but crucial.

### AI works best with specific questions

Vague questions got vague answers. But when I described exactly what bug I was seeing ("I have to click twice before the page changes"), I got useful solutions immediately.

### Small UX details matter

Things like the countdown redirect and message placement make the app feel more professional even though the functionality is the same.

### Form patterns in Streamlit

Using `st.form` to batch inputs together makes validation way cleaner than handling each input separately. Learned to validate everything before taking action (registering user, updating session state, etc.).

---

## Growth This Semester

I'd used Streamlit a few times before but only for simple stuff. This was my first time building something with authentication, managing multiple screens, and coordinating session state across everything.

Biggest thing I learned was how to use AI effectively and not just copy-pasting code, but asking specific questions about problems I was facing, understanding the solutions, and implementing them myself. Also got better at debugging when things broke.

---

## If I Had More Time

- Add an actual database
- Hash passwords with bcrypt
- Add email verification for registration
- Build password reset flow
- Make metrics track something real
- Let users edit their profiles
- Improve the styling (maybe custom theme)
- Add unit tests for auth functions
- Deploy it (Streamlit Cloud)

---

## Honest Take

This project went pretty smoothly once I figured out the session state patterns. The double-click bug was annoying but `st.rerun()` fixed it. Overall I'm happy with how it turned out. It's functional, the UX is decent, and I learned a lot about managing state in Streamlit.

Biggest weakness is definitely the lack of persistent storage and password security, but for a demo project it does what it's supposed to do.