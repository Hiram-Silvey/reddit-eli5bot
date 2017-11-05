#import simpli5
import praw
import re

reddit = praw.Reddit('eli5bot')
subreddit = reddit.subreddit("all")

for comment in subreddit.stream.comments():
    if re.search("eli5", comment.body, re.IGNORECASE):
        parent_comment = comment.parent.body
        transformed = simpli5.parser.simpli5(simpli5.worker.smmrize(parent_comment))
        comment.reply(transformed)
        print(transformed)
