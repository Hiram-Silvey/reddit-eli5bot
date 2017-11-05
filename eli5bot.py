import simpli5.parser as smpl
import praw
import re

reddit = praw.Reddit('eli5bot')
subreddit = reddit.subreddit("all")

for comment in subreddit.stream.comments():
    if re.search("i", comment.body, re.IGNORECASE):
        parent = comment.parent()
        if isinstance(parent, praw.models.Submission):
            continue
        parent_comment = comment.parent().body
        transformed = smpl.simpli5(smpl.smmrize(parent_comment))
        #comment.reply(transformed)
        print(transformed)
