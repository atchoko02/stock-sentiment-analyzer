import praw
from config import REDDIT_CLIENT_ID, REDDIT_SECRET, USER_AGENT

reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_SECRET,
        user_agent=USER_AGENT,
    )

# fetches recent reddit posts about a stock from some subreddits
def fetch_reddit_posts(ticker: str, company_name: str, limit: int = 100):
    # use praw api or whatever to fetch reddit psots
    query = f'{ticker} OR ${ticker} OR {ticker.upper()} OR ${ticker.upper()} OR {company_name}'
    subreddits = ['stocks', 'wallstreetbets', 'investing', 'stockmarket', 'daytrading']
    posts = []
    for sub in subreddits:
        subreddit = reddit.subreddit(sub)
        res = subreddit.search(query, sort='new', time_filter='day', limit=limit)
        
        for post in res:
            posts.append({
                'title': post.title,
                'url': post.url,
                'text': post.selftext,
                'score': post.score,
                'subreddit': sub
            })
    
    return posts

