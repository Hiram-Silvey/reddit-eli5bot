import simpli5
import praw
import re

reddit = praw.Reddit('eli5bot')

subreddit = reddit.subreddit("all")

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("!eli5", comment.body, re.IGNORECASE):
            # get parent comment and run it through SMMRY -> simpli5
            # comment.reply(the result)
            # print(the result)
            


