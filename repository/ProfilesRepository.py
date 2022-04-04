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
        query = 'insert into profilo_instagram (username) values (:username)'
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


    def get_profiles_for_crawling(self, amount):
        # da fare con transazioni
        pass
