from .models import SocialChannel, Post
from abc import ABC
import datetime


# each social channel has a type
# and the current number of followers
# SocialChannel = tuple[str, int]

# each post has a message and the timestamp when it should be posted
# Post = tuple[str, int]

def post_a_message(channel: SocialChannel, post: Post) -> None:
    channel.post(post)


def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
    for post in posts:
        message, timestamp = post
        for channel in channels:
            if timestamp <= datetime:
                post_a_message(channel, message)


def main():
    youtube_chanel = SocialChannel("Youtube", 500)
    facebook_chanel = SocialChannel("Facebook", 20)
    twitter_chanel = SocialChannel("Twitter", 1000)

    greeting = Post("Hello, welcome!", datetime.datetime(2024, 10, 18))
    invite = Post("Feel free to invite your friend to get a prize", datetime.datetime(2024, 10, 18))
    happy_tg = Post("Happy thanksgiving day!", datetime.datetime(2024, 10, 18))

    post_a_message(youtube_chanel, greeting)
    post_a_message(facebook_chanel, invite)
    post_a_message(twitter_chanel, happy_tg)


if __name__ == "__main__":
    main()
git gti