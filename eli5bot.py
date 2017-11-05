import simpli5.parser as smpl
import praw
import re

reddit = praw.Reddit('eli5bot')
subreddit = reddit.subreddit("all")

SIGNATURE = 'beep boop. I am the eli5bot. I attempt to translate things to simpler english and link relevant wiki articles.'

for comment in subreddit.stream.comments():
    if re.search("e", comment.body, re.IGNORECASE):
        parent = comment.parent()
        if isinstance(parent, praw.models.Submission):
            continue
        parent_comment = comment.parent().body
        print '\nbefore:'
        print parent_comment
        transformed = smpl.simpli5(smpl.smmrize(parent_comment))
        #comment.reply(transformed)
        print '\nafter:'
        print transformed
        result = '> ' + transformed + '\n*****\nI am eli5bot. I attempt to simplify text and provide relevant wiki links. Beep boop.'
        break
