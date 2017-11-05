import simpli5.parser as smpl
import praw
import re
import time
reddit = praw.Reddit('eli5bot')
subreddit = reddit.subreddit("science")

for comment in subreddit.stream.comments():
    if re.search("eli5", comment.body, re.IGNORECASE):
        parent = comment.parent()
        if isinstance(parent, praw.models.Submission):
            continue
        parent_comment = comment.parent().body
        transformed = smpl.simpli5(smpl.smmrize(parent_comment))
        try:
            comment.reply(transformed)

        except:
            print "Need to wait for at least 10 minutes to make another comment"
            time.sleep(600)
            comment.reply(transformed)
        print(transformed)
