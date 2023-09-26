# RIP BOT
# FUCK /u/spez

# chicanerybot
Reddit bot that responds with "Yup!", "Yapp" and variants to comments containing "fuck" in /r/okbuddychicanery.

Requirements:
`Docker`

Provide your own Reddit credentials in praw.ini then run

`sudo docker build -t chicanerybot -f Dockerfile .`

and

`sudo docker run -d --name chicanerybot chicanerybot`

[Thanks Kalju Jake Nekvasil!](https://knekvasil.medium.com/deploying-a-reddit-bot-on-heroku-with-docker-6a3404a49093)
