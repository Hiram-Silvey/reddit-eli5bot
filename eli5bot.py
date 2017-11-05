import simpli5.parser as smpl
import praw
import re
import time
reddit = praw.Reddit('eli5bot')
subreddit = reddit.subreddit("test")

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

        print '\nafter:'
        result = '> ' + transformed + '\n*****\nI am eli5bot. I attempt to simplify text and provide relevant wiki links. Beep boop.'
        print result
        #try:
        #    comment.reply(result)
        #    break

        #except:
        #    print "Need to wait for at least 10 minutes to make another comment"
        #    time.sleep(600)
        #    comment.reply(transformed)

