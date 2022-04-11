from crawler.profiles.ProfileForCrawling import ProfileForCrawling


class ProfileFactory:
    @staticmethod
    def build_from_db(db_data: dict) -> ProfileForCrawling:
        """
        Builds a ProfileForCrawling object from a dictionary containing the data from the database obtained by a query
        like: 'SELECT * FROM profilo_instagram WHERE username = ?'.

        :param db_data: A dictionary containing the data from the database.
        :return: A ProfileForCrawling object corresponding to the data from the database.
        """
        if db_data['data_ultimo_check'] is True:
            return ProfileForCrawling(db_data['username'], None, db_data['post_visti'],
                                      db_data['post_utili'])
        else:
            return ProfileForCrawling(db_data['username'], db_data['data_ultimo_check'], db_data['post_visti'],
                                      db_data['post_utili'])
