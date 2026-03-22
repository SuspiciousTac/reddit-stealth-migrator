\# Reddit Stealth Account Migrator (Cookie-Based)



A lightweight, stealth-focused tool to migrate your Reddit data to a new account using your official Reddit Data Export. This tool avoids the official API to minimize the risk of shadowbans on new accounts.



\## 🚀 Why This is Better Than API Tools

Most migrators use the official Reddit API (PRAW). This tool is different:

\- \*\*No Developer App Needed:\*\* No need to register a "bot" with Reddit.

\- \*\*No API Limits:\*\* Browses like a human using Playwright, avoiding strict rate limits.

\- \*\*Stealth-First:\*\* Injects your active `reddit\_session` cookie into a real browser instance.



\## 🛡️ Safety \& Spam Protection

The CSV files chosen for this script (\*\*Subreddits, Saved Posts, Saved Comments, and Upvotes\*\*) were specifically selected because they are the \*\*safest for avoiding spam filters.\*\*

\- \*\*Why only these?\*\* Other files in your export (like `posts.csv` or `comments.csv`) contain raw text. Automating the re-posting of hundreds of old comments onto a new account is the fastest way to get flagged as a "Spam Bot."

\- \*\*Ghosting Prevention:\*\* By focusing on "Engagements" (Joins and Saves) rather than "Submissions," your account builds a natural-looking history that is much less likely to trigger a shadowban.



\## 🤖 Disclaimer for Beginners

\*\*If you are not a coder, don't worry!\*\* You can use AI (like Gemini, ChatGPT, or Claude) to help you run this script. 

\- If you see an error, just copy and paste the error into your AI assistant and ask, "How do I fix this in my Python script?"

\- AI is excellent at helping you find your cookie or setting up your folder structure if you get confused. It was a huge help in building this!



\## 📦 What this script migrates:

The script runs in 4 distinct phases:

1\. \*\*Phase 1: Subreddits\*\* (Joins all communities from `subscribed\_subreddits.csv`)

2\. \*\*Phase 2: Saved Posts\*\* (Saves all posts from `saved\_posts.csv`)

3\. \*\*Phase 3: Saved Comments\*\* (Saves all comments from `saved\_comments.csv`)

4\. \*\*Phase 4: Upvotes\*\* (Upvotes your history from `post\_votes.csv` to train your new Home feed)



\## 🛠️ How to use

1\. \*\*Request Data:\*\* Request your data export from Reddit Settings. Once you receive the ZIP, extract it.

2\. \*\*Setup Environment:\*\*

&#x20;  ```bash

&#x20;  pip install -r requirements.txt

&#x20;  playwright install chromium

3\. Add Your Data

Place your extracted `.csv` files from the Reddit export into this project folder. The script specifically looks for:

\* `subscribed\_subreddits.csv`

\* `saved\_posts.csv`

\* `saved\_comments.csv`

\* `post\_votes.csv`



4\. Authenticate (Cookie Method)

Instead of an API key, this script uses your active session.

1\. Open Reddit in your browser and log in to your \*\*NEW\*\* account.

2\. Press `F12` (or Right-Click > Inspect) to open Developer Tools.

3\. Navigate to the \*\*Application\*\* tab (Chrome/Edge) or \*\*Storage\*\* tab (Firefox).

4\. In the left sidebar, click \*\*Cookies\*\* -> `https://www.reddit.com`.

5\. Find the row named `reddit\_session`.

6\. Copy the long text string in the \*\*Value\*\* column.

7\. Open `reddit\_sync.py` and paste that string into the `SESSION\_COOKIE` variable:

&#x20;  ```python

&#x20;  SESSION\_COOKIE = "your\_cookie\_here"

5\. Run the Script

Open your Command Prompt or Terminal in the project folder and run:



Bash

python reddit\_sync.py





