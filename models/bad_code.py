"""Logic related to User."""
from datetime import datetime


class User:
    """System user, does important things."""

    # static typing is good to avoid mistakes
    def __init__(self, first_name: str, last_name: str) -> None:
        """Init."""
        self.first_name = first_name
        self.last_name = last_name

    # -> str is something for IDE so that if a method returns non-str pycharm will use russian swear words
    def get_full_name(self) -> str:
        """Returns first and last name."""
        return self.first_name + " " + self.last_name

    def is_first_name_good(self) -> bool:
        """Checks if a first name is neither Doh nor A"""
        is_good = (
            True
            if self.first_name and self.first_name is not None and self.first_name != "Doh" and self.first_name != "A"
            else False
        )
        return is_good

    @staticmethod
    def user_time() -> datetime:
        """Returns user's date and time"""
        return datetime.now()


user = User("Bob", "Bobob")

if user.get_full_name().upper().split(" ")[0] == "Alex":
    print("Some important logic")
print("Works")

my_new_name = "Alex " + user.get_full_name()
