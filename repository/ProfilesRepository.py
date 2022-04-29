from typing import List

from repository.DatabaseHandler import DatabaseHandler


class ProfilesRepository:
    def __init__(self) -> None:
        self.__db = DatabaseHandler('crawler_test')

    def __update_last_time_check(self, username: str):
        username_param = {'name': 'username', 'value': {'stringValue': username}}
        query = 'update profilo_instagram set data_ultimo_check = current_timestamp where username = :username'
        paramset = [username_param]
        return self.__db.do_write_query(query, paramset)

    def select_profile(self, username: str):
        username_param = {'name': 'username', 'value': {'stringValue': username}}
        query = 'select * from profilo_instagram where username = :username'
        paramset = [username_param]
        return self.__db.do_read_query(query, paramset)

    def insert_profile(self, username: str):
        username_param = {'name': 'username', 'value': {'stringValue': username}}
        query = 'insert into profilo_instagram (username, level) values (:username, 1)'
        paramset = [username_param]
        return self.__db.do_write_query(query, paramset)

    def insert_profiles_list(self, profile_list: List[str]):
        paramset = []
        i = 0
        query = 'insert into profilo_instagram (username) values '
        for profile in profile_list:
            paramset.append({'name': f'username{i}', 'value': {'stringValue': profile}})
            query += f'(:username{i}), '
            i += 1
        query = query[:-2]
        return self.__db.do_write_query(query, paramset)

    def get_profile_for_crawling_level_1(self):
        query = 'select * from profilo_instagram where level = 1 order by data_ultimo_check, username limit 1'
        response = self.__db.do_read_query(query)
        profile = response[0]['username']
        self.__update_last_time_check(profile)
        return response

    def update_post_profile(self, username: str, post_viewed: int, post_useful: int):
        """
        Update a profile by adding the amount of posts viewed and useful.

        :param username: Username of the profile to update
        :param post_viewed: Amount of posts viewed to add
        :param post_useful: Amount of posts useful to add

        :return: Response from the database
        """
        username_param = {'name': 'username', 'value': {'stringValue': username}}
        post_visti_param = {'name': 'post_viewed', 'value': {'longValue': post_viewed}}
        post_utili_param = {'name': 'post_useful', 'value': {'longValue': post_useful}}
        query = 'update profilo_instagram set post_visti = post_visti + :post_viewed, post_utili = post_utili + :post_useful where username = :username'
        paramset = [username_param, post_visti_param, post_utili_param]
        return self.__db.do_write_query(query, paramset)
