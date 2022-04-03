from repository.ProfilesRepository import ProfilesRepository


class FacadeAddProfile:

    def __init__(self, profile):
        self.__profile = profile
        self.__repository = ProfilesRepository()

    def add_profile(self) -> int:
        # check if the profile is already in the database
        if self.__repository.select_profile(self.__profile):
            return 1

        # check if exists and is public
