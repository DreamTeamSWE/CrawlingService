from repository.DatabaseHandler import DatabaseHandler


class ProfilesRepository:
    def __init__(self) -> None:
        self.__db = DatabaseHandler('crawler_test')

    def select_profile(self, username: str) -> dict:
        username_param = {'name': 'username', 'value': {'stringValue': username}}
        query = 'select * from profilo_instagram where username = :username'
        paramset = [username_param]
        return self.__db.do_read_query(query, paramset)

    def insert_profile(self, username: str):
        username_param = {'name': 'username', 'value': {'stringValue': username}}
        query = 'insert into profilo_instagram (username) values (:username)'
        paramset = [username_param]
        return self.__db.do_write_query(query, paramset)

    def get_profiles_for_crawling(self, amount):
        # da fare con transazioni
        pass
