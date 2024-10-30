import datetime

from models import Post, SocialChannel

# each social channel has a type
# and the current number of followers
# SocialChannel = tuple[str, int]

# each post has a message and the timestamp when it should be posted
# Post = tuple[str, int]


def post_a_message(channel: SocialChannel, post: Post) -> None:
    channel.post(post)


posts_list: list[Post] = []
channels_list: list[SocialChannel] = []


def post_dispatcher(message: str, timestamp: datetime) -> Post:
    post = Post(message=message, timestamp=timestamp)
    posts_list.append(post)
    return post


def channel_dispatcher(type_: str, followers: int) -> SocialChannel:
    channel = SocialChannel(type_=type_, followers=followers)
    channels_list.append(channel)
    return channel


def process_schedule(
    posts: list[Post], channels: list[SocialChannel], debug: bool = False
) -> None:
    # enable debug to see if it's too early to post
    for post in posts:
        for channel in channels:
            if post.timestamp <= datetime.datetime.now():
                post_a_message(channel, post)
            else:
                if debug:
                    print(f"it's too early to post {post.message}")


def main():
    channel_dispatcher("Youtube", 500)
    channel_dispatcher("Facebook", 20)
    channel_dispatcher("Twitter", 1000)

    post_dispatcher("Hello, welcome!", datetime.datetime(2024, 10, 16))
    post_dispatcher(
        "Feel free to invite your friend to get a prize",
        datetime.datetime(2024, 10, 18),
    )
    post_dispatcher("Happy thanksgiving day!", datetime.datetime(2024, 10, 19))

    process_schedule(posts_list, channels_list)

    # post_a_message(youtube_chanel, greeting)
    # post_a_message(facebook_chanel, invite)
    # post_a_message(twitter_chanel, happy_tg)


if __name__ == "__main__":
    main()
