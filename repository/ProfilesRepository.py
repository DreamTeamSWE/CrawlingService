from typing import List

from repository.DatabaseHandler import DatabaseHandler


class ProfilesRepository:
    def __init__(self) -> None:
        self.__db = DatabaseHandler('crawler_test')

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

    def get_profiles_for_crawling_all_levels(self, amount):
        # TODO: da sistemare, capire come evitare dirty read
        amount_param = {'name': 'amount', 'value': {'longValue': amount}}
        query = 'select * from profilo_instagram order by data_ultimo_check limit :amount'
        paramset = [amount_param]
        response = self.__db.do_read_query(query, paramset)
        profiles = []
        for x in response:
            profiles.append(x['username'])
        return profiles

    def update_post_profile(self, username: str, post_viewed: int, post_useful: int):
        """
        update a profile by adding the amount of posts viewed and useful.

        :type username: str
        :param username: Unique identifier for a location
        :type post_viewed: int
        :param post_viewed: Amount of posts viewed to add
        :type post_useful: int
        :param post_useful: Amount of posts useful to add
        :rtype dict
        :returns Response from the database
        """
        username_param = {'name': 'username', 'value': {'stringValue': username}}
        post_visti_param = {'name': 'post_viewed', 'value': {'longValue': post_viewed}}
        post_utili_param = {'name': 'post_useful', 'value': {'longValue': post_useful}}
        query = 'update profilo_instagram set post_visti = post_visti + :post_viewed, post_utili = post_utili + :post_useful where username = :username'
        paramset = [username_param, post_visti_param, post_utili_param]
        return self.__db.do_write_query(query, paramset)
