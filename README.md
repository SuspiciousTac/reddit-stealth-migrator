# Reddit Stealth Account Migrator (Cookie-Based)

A simple, stealthy tool to help you move your Reddit data to a brand-new account using your official Reddit Data Export. This tool skips the official Reddit API entirely, which helps keep your new account safe from shadowbans.

## 🚀 Why use this instead of other tools?

Most migration tools use the official Reddit API (PRAW), which can easily flag new accounts. This tool works differently:

- **No "Bot" Apps Needed:** You don't have to register a developer account with Reddit.
- **No API Limits:** It uses Playwright to browse Reddit just like a real person would, so you don't hit strict rate limits.
- **Stealthy:** It uses your actual `reddit_session` cookie to log in, making it look like you are just using your browser.

## 🛡️ Safety & Spam Protection

I’ve carefully chosen the data types for this script (Subreddits, Saved Posts, Saved Comments, and Upvotes) because they are the **safest way to migrate without triggering spam filters.**

- **Why avoid other files?** Files like `posts.csv` or `comments.csv` contain your old text. If a new account suddenly posts hundreds of old comments at once, Reddit will almost certainly mark you as a "Spam Bot."
- **Preventing Ghosting:** By sticking to "Engagements" like joining communities and saving posts, your account builds a natural history that looks legitimate, helping you stay under the radar.

## 🤖 New to coding? No problem!

**Don't worry if you aren't a programmer.** You can easily use AI tools like ChatGPT, Claude, or Gemini to guide you through the setup.

- If you run into an error message, just copy and paste it into an AI chat and ask: "How do I fix this in my Python script?"
- AI is also great at helping you find your cookies or explaining how to set up your files if you get stuck.

## 📦 What this script migrates

The process runs in 4 easy steps:

1. **Phase 1: Subreddits** (Joins all your old communities from `subscribed_subreddits.csv`)
2. **Phase 2: Saved Posts** (Saves your old posts from `saved_posts.csv`)
3. **Phase 3: Saved Comments** (Saves your old comments from `saved_comments.csv`)
4. **Phase 4: Upvotes** (Upvotes your history from `post_votes.csv` to help train your new feed)

## 🛠️ How to get started

1. **Request Your Data:** Go to your Reddit settings and request your data export. Once you get the ZIP file via email, unzip it.
2. **Get Ready:** Open your terminal in this folder and run:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
   ```
3. **Add Your Files:** Place these four files from your Reddit export folder into this project folder:
   - `subscribed_subreddits.csv`
   - `saved_posts.csv`
   - `saved_comments.csv`
   - `post_votes.csv`
4. **Log In (The Cookie Way):**
   - Log in to your **new** Reddit account in your browser.
   - Press `F12` (or Right-Click > Inspect) to open the developer menu.
   - Go to the **Application** tab (Chrome/Edge) or **Storage** tab (Firefox).
   - Look for **Cookies** on the left and select `https://www.reddit.com`.
   - Find `reddit_session`, right-click it, and copy the long string of text in the **Value** column.
   - Open `reddit_sync.py` and paste that code into the `SESSION_COOKIE` line.
5. **Run the Script:**
   In your terminal, simply type:
   ```bash
   python reddit_sync.py
   ```
