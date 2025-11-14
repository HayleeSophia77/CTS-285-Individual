# Vibe Coding Assignment

## ASSIGNMENT: VIBE CODING YOUR FIRST WEB APP

**ORANGE LAB:** AI Fundamentals  
**Estimated Time:** 4-6 hours  
**Collaboration:** Individual (but discuss strategies with classmates!)

## WHAT YOU'RE LEARNING

This assignment teaches you to work with AI to build something functional quickly, while also learning when AI helps and when it struggles. By the end, you'll understand:

- How to collaborate with AI tools for rapid prototyping
- The difference between "it works" and "I understand why it works"
- When to trust AI suggestions and when to question them
- How different frameworks affect what's possible

**Important:** This isn't about becoming a web developer. It's about understanding how to use AI as a tool while staying in control of the process.

## PART 1: THE AI'S CHOICE (2-3 hours)

### Your Mission
Build a simple interactive web application using ONLY prompts. Let the AI decide how to build it.

### Step 1: Pick Your Game (15 minutes)
Choose ONE simple game or interactive tool:

**Option A: Tic-Tac-Toe**
- Two players take turns
- Check for winners
- Reset button

**Option B: Dice Game (Craps)**
- Roll two dice
- Display results
- Keep score

**Option C: Number Guessing Game**
- Computer picks random number 1-100
- Player guesses
- Give "higher/lower" hints

**Option D: Simple Calculator**
- Basic operations (+, -, ×, ÷)
- Display running total
- Clear button

**Option E: Your Choice**
- Must be similarly simple
- Must be interactive (not just display)
- Get instructor approval first

### Step 2: First Prompt (Start Simple!)
Open your AI tool of choice (Gemini with Canvas, ChatGPT, Claude, etc.) and try something like:
```
"Build me a complete, working [your game] that runs in a web browser. 
Make it a single HTML file that I can just open and use. 
Include all the JavaScript and CSS needed."
```

**Important:** Save this prompt and all your follow-up prompts! You'll document them later.

### Step 3: Test & Iterate (1-2 hours)
1. Copy the AI's code into a file called `attempt1.html`
2. Open it in your browser - does it work?
3. If it works: Great! Try to break it. Test edge cases.
4. If it doesn't work:
   - Ask the AI to fix the specific problem
   - Try rephrasing your request
   - Ask for explanations of what the code does
5. Keep making new files: `attempt2.html`, `attempt3.html`, etc.

**Document your iterations!** For each attempt, note:
- What you asked the AI to change
- Whether it worked
- What you learned

### Step 4: Make It Yours (30 minutes)
Once you have something working, ask the AI to:
- Change the colors or styling
- Add a feature (like score tracking)
- Make error messages more helpful
- Add instructions for players

**Goal:** Get it to a point where someone else could use it without your help.

## PART 2: THE FRAMEWORK EXPERIMENT (1-2 hours)

### Your Mission
Discover what a "Single Page Application" (SPA) is and try building your game using a framework designed for SPAs.

### Step 1: Ask the AI About SPAs
Before you start coding, have a conversation with your AI:
```
"What is a Single Page Application? 
What frameworks are commonly used to build SPAs?
Which one would be best for rebuilding my [game name]? 
Explain why."
```

Take notes on what it recommends. Common frameworks it might suggest:
- React
- Vue
- Svelte
- Vanilla JavaScript (no framework)

### Step 2: The Framework Challenge
Now ask the AI to rebuild your game using the framework it recommended:
```
"Rebuild my [game name] as a Single Page Application using [framework name]. 
Create a complete working version I can test. 
Explain what's different about using [framework] for this."
```

### Step 3: Experience the Difference
You'll probably notice:
- More complexity (maybe more files, build steps, setup)
- Different way of thinking about the problem
- Possibly harder to get working
- Maybe more powerful features?

**This is the lesson:** Sometimes "better" tools make simple things harder.

### Step 4: Get It Working (Or Don't!)
Try to get the SPA version working. But here's the thing: **it's okay if you don't succeed.**

The learning happens whether it works or not:
- **If it works:** Why was it harder? Was it worth it? When would you use this approach?
- **If it doesn't:** What got in the way? When did you hit the wall? What was too complex?

**Document this experience!** Your struggles are valuable data.

## PART 3: REFLECTION & SUBMISSION (30-45 minutes)

### Create Your Submission Folder
Make a folder called `vibe-coding-[yourname]` with these files:

### Required File 1: PROMPTS.md
Document your key prompts (at least 5). For each one, note:
- What you asked
- What worked about the AI's response
- What didn't work
- What you learned

Format:
```markdown
# My Vibe Coding Prompts

## Prompt 1: Initial Build
**What I asked:** "Build me a tic-tac-toe game..."

**What the AI did:** It generated a complete HTML file with CSS and JavaScript

**What worked:** The file opened in my browser and showed a grid

**What didn't work:** Clicking squares didn't do anything - the click handlers were broken

**What I learned:** AI can create the structure quickly but may miss functionality

## Prompt 2: Fix Click Handlers
[Continue with more prompts...]
```

### Required File 2: Your Best Working Version
Include your best working version from Part 1:
- `[gamename]-final.html` (e.g., `tictactoe-final.html`)

If you got Part 2 working, include those files in a subfolder:
- `spa-version/` folder with all necessary files

### Required File 3: REFLECTION.md
Answer these questions (1-2 paragraphs each):

**1. The AI as Collaborator**
- When did the AI help you most?
- When did it frustrate you most?
- What surprised you about working with AI?

**2. The Framework Experiment**
- What did the AI recommend and why?
- What was different about building an SPA?
- Which approach felt better for YOUR game? Why?
- If you were building something bigger, would your answer change?

**3. The "Vibe Coding Ceiling"**
- Did you hit a point where AI couldn't help anymore?
- When did you realize you needed to understand the code yourself?
- What would you do differently next time?

**4. Growth Moment**
- What did this teach you about AI tools?
- What did this teach you about web development?
- What question do you have now that you didn't have before?

## SUBMITTING TO GITHUB

### The Simple Way (No Command Line Needed!)
1. Go to your CSC-113 GitHub repository
2. Click "Add file" → "Upload files"
3. Drag your entire `vibe-coding-[yourname]` folder onto the page
4. Add commit message: "Complete vibe coding assignment"
5. Click "Commit changes"
