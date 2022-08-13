import praw
import random
import re

def run_bot():
    bot_message_disclaimer = """\n &nbsp; \n *** \n ^(*Beep boop. I am a bot, 
    and this action was performed automatically.*)"""
    reddit = praw.Reddit('chicanerybot')
    subreddit = reddit.subreddit("okbuddychicanery")
    replied_comments = []

    with open("replied_comments.txt", "r") as f:
        replied_comments = f.read()
        replied_comments = replied_comments.split("\n")
        replied_comments = list(filter(None, replied_comments))

    for comment in subreddit.stream.comments():
        if comment.id not in replied_comments:
            if re.search("fuck", comment.body, re.IGNORECASE):
                response = str(random.choice(['Yep!', 'Yup', 'Yup! Yup!', 'Yapp']))
                comment.reply(response + bot_message_disclaimer)
                replied_comments.append(comment.id)

                with open("replied_comments.txt", "w") as f:
                    for comment_id in replied_comments:
                        f.write(comment_id + "\n")

def main():
    run_bot()


if __name__ == "__main__":
    main()
