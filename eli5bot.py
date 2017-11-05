import simpli5.parser as smpl
import praw
import time
import pickle
import os


f = open("red_list.txt", 'w+')
try:
    red_list=pickle.load(f)
except EOFError:
    red_list = []

reddit = praw.Reddit('eli5bot')
subreddit = reddit.subreddit("all")

SIGNATURE = 'beep boop. I am the eli5bot. I attempt to translate things to simpler english and link relevant wiki articles.'

for comment in subreddit.stream.comments():

    if '!eli5' in comment.body.lower():
        print "eli5bot is summoned!"
        parent = comment.parent()
        if isinstance(parent, praw.models.Submission) or parent.fullname is red_list:
            print "This comment can be skipped."
            continue

        parent_comment = comment.parent().body
        print '\nbefore:'
        print parent_comment
        transformed = smpl.simpli5(smpl.smmrize(parent_comment))

        print '\nafter:'
        result = '> ' + transformed + '\n*****\nI am eli5bot. I attempt to simplify text and provide relevant wiki links. Beep boop.'
        print result
        try:
            comment.reply(result)
            f.write(comment.fullname)
        except:
            print "Need to wait for at least 10 minutes to make another comment"
            time.sleep(600)
            comment.reply(result)
