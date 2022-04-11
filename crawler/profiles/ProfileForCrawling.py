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
        """
        Get the username of the profile
        """
        return self.__username

    def get_last_time_checked(self):
        """
        Get the last time the profile was checked
        """
        return self.__last_time_checked

    def get_viewed_posts(self):
        """
        Get the number of posts viewed for this profile
        """
        return self.__viewed_posts

    def get_usefull_posts(self):
        """
        Get the number of usefull posts viewed for this profile
        """
        return self.__usefull_posts

    # Setters

    def set_last_time_checked(self, last_time_checked):
        """
        Set the last time the profile was checked
        """
        self.__last_time_checked = last_time_checked

    def set_viewed_posts(self, viewed_posts):
        """
        Set the number of posts viewed for this profile
        """
        self.__viewed_posts = viewed_posts

    def set_usefull_posts(self, usefull_posts):
        """
        Set the number of usefull posts viewed for this profile
        """
        self.__usefull_posts = usefull_posts

    def is_crawable(self) -> bool:
        """
        Check if the profile posts an acceptable amount of contents related to food
        """
        if self.__viewed_posts < 30:
            return True
        else:
            return self.__usefull_posts > 0

    def add_not_usefull_post(self):
        """
        Update a profile after a post was not usefull
        """
        self.__viewed_posts += 1

    def add_usefull_post(self):
        """
        Update a profile after a post was usefull
        """
        self.__usefull_posts += 1
        self.__viewed_posts += 1
