"""
REDDIT STEALTH MIGRATOR (NON-API)
---------------------------------
Mechanism: Playwright Browser Automation (Cookie-Based)
Why not API?: Official API usage is heavily monitored and requires app registration. 
              This script mimics human clicks via browser cookies for maximum safety.
"""

import pandas as pd
import asyncio
import random
import os
import time
from playwright.async_api import async_playwright

# --- CONFIGURATION ---
# IMPORTANT: Do not share your script if this line contains your real cookie!
SESSION_COOKIE = "PASTE_YOUR_REDDIT_SESSION_COOKIE_HERE"

def get_progress(phase):
    file = f"progress_{phase}.txt"
    return int(open(file, "r").read().strip()) if os.path.exists(file) else 0

def save_progress(phase, idx):
    with open(f"progress_{phase}.txt", "w") as f: f.write(str(idx))

def format_time(seconds):
    mins, secs = divmod(int(seconds), 60)
    return f"{mins}m {secs}s"

async def run_sync():
    if SESSION_COOKIE == "PASTE_YOUR_REDDIT_SESSION_COOKIE_HERE":
        print("Error: You must paste your reddit_session cookie into the script first!")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/122.0.0.0 Safari/537.36")
        
        await context.add_cookies([{
            "name": "reddit_session", 
            "value": SESSION_COOKIE, 
            "domain": ".reddit.com", 
            "path": "/", 
            "secure": True, 
            "httpOnly": True
        }])
        
        page = await context.new_page()

        # PHASE 1: SUBREDDITS
        if os.path.exists('subscribed_subreddits.csv'):
            df = pd.read_csv('subscribed_subreddits.csv')
            last = get_progress("subs")
            if last < len(df):
                print(f"\n>> PHASE 1: Subreddits ({len(df)} total)")
                start_t = time.time()
                for i, row in df.iloc[last:].iterrows():
                    curr_idx = i + 1
                    sub = row['subreddit']
                    print(f"[{curr_idx}/{len(df)}] r/{sub}...", end=" ", flush=True)
                    try:
                        await page.goto(f"https://www.reddit.com/r/{sub}/", timeout=30000)
                        await asyncio.sleep(random.uniform(3, 5))
                        btn = page.locator('button:has-text("Join")').first
                        if await btn.is_visible():
                            await btn.click()
                            print("JOINED", end=" ")
                        else: print("SKIP", end=" ")
                        save_progress("subs", curr_idx)
                    except: print("TIMEOUT", end=" ")
                    
                    elapsed = time.time() - start_t
                    avg = elapsed / (curr_idx - last)
                    rem = avg * (len(df) - curr_idx)
                    print(f"| Est. Left: {format_time(rem)}")
                    await asyncio.sleep(random.uniform(5, 10))

        # PHASE 2: SAVED POSTS
        if os.path.exists('saved_posts.csv'):
            df = pd.read_csv('saved_posts.csv')
            last = get_progress("saved")
            if last < len(df):
                print(f"\n>> PHASE 2: Saving Posts ({len(df)} total)")
                start_t = time.time()
                for i, row in df.iloc[last:].iterrows():
                    curr_idx = i + 1
                    print(f"[{curr_idx}/{len(df)}] Saving {row['id']}...", end=" ", flush=True)
                    try:
                        await page.goto(row['permalink'], timeout=30000)
                        await asyncio.sleep(random.uniform(4, 7))
                        save_btn = page.locator('button[aria-label="save"]').first
                        if await save_btn.is_visible():
                            await save_btn.click()
                            print("SAVED", end=" ")
                        save_progress("saved", curr_idx)
                    except: print("ERROR", end=" ")
                    
                    elapsed = time.time() - start_t
                    avg = elapsed / (curr_idx - last)
                    rem = avg * (len(df) - curr_idx)
                    print(f"| Est. Left: {format_time(rem)}")
                    await asyncio.sleep(random.uniform(8, 15))

        # PHASE 3: POST VOTES
        if os.path.exists('post_votes.csv'):
            df = pd.read_csv('post_votes.csv')
            df = df[df['direction'] == 'up']
            last = get_progress("votes")
            if last < len(df):
                print(f"\n>> PHASE 3: Syncing Upvotes ({len(df)} total)")
                start_t = time.time()
                for i, row in df.iloc[last:].iterrows():
                    curr_idx = i + 1
                    print(f"[{curr_idx}/{len(df)}] Upvoting {row['id']}...", end=" ", flush=True)
                    try:
                        await page.goto(row['permalink'], timeout=30000)
                        await asyncio.sleep(random.uniform(5, 8))
                        btn = page.locator('button[aria-label="upvote"]').first
                        if await btn.is_visible() and await btn.get_attribute("aria-pressed") != "true":
                            await btn.click()
                            print("VOTED", end=" ")
                        save_progress("votes", curr_idx)
                    except: print("ERROR", end=" ")
                    
                    elapsed = time.time() - start_t
                    avg = elapsed / (curr_idx - last)
                    rem = avg * (len(df) - curr_idx)
                    print(f"| Est. Left: {format_time(rem)}")
                    await asyncio.sleep(random.uniform(10, 20))

        print("\n\n[SUCCESS] Sync complete!")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_sync())