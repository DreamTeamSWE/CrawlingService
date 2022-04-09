from datetime import datetime


class ProfileForCrawling:
    def __init__(self, username, last_time_checked: str = None, viewed_posts=0, usefull_posts=0):
        self.__username = username
        if last_time_checked is None:
            self.__last_time_checked = None
        else:
            self.__last_time_checked = datetime.strptime(last_time_checked, '%Y-%m-%d %H:%M:%S')
        self.__viewed_posts = viewed_posts
        self.__usefull_posts = usefull_posts

    # Getters
    def get_username(self):
        return self.__username

    def get_last_time_checked(self):
        return self.__last_time_checked

    def get_viewed_posts(self):
        return self.__viewed_posts

    def get_usefull_posts(self):
        return self.__usefull_posts

    # Setters

    def set_last_time_checked(self, last_time_checked):
        self.__last_time_checked = last_time_checked

    def set_viewed_posts(self, viewed_posts):
        self.__viewed_posts = viewed_posts

    def set_usefull_posts(self, usefull_posts):
        self.__usefull_posts = usefull_posts

    def is_crawable(self) -> bool:
        if self.__viewed_posts < 30:
            return True
        else:
            return self.__usefull_posts > 0

    def add_not_usefull_post(self):
        self.__viewed_posts += 1

    def add_usefull_post(self):
        self.__usefull_posts += 1
        self.__viewed_posts += 1
