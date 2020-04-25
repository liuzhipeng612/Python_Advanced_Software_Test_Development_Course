import random
import time


def sleep(n_secs):
    time.sleep(n_secs)


def get_user_agent():
    user_agent = ["Mozilla/5.0 Winter Swimming1", "Mozilla/5.0 Winter Swimming2", "Mozilla/5.0 Winter Swimming3",
                  "Mozilla/5.0 Winter Swimming4"]
    return random.choice(user_agent)


if __name__ == "__main__":
    print(get_user_agent())
