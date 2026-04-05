#user_repository.py
from User import User
users = [
    User("admin","admin","Михаил Ануфрев"),
    User("winter", "is_near", "Джон Сноу"),
    User("jane", "password", "Джейн Смит"),
    User("bob", "secret123", "Боб Джонс"),
    User("susan", "p@ssw0rd", "Сьюзан Вонг"),
]
users_repos = {user.get_login(): user for user in users}
def get_user_by_login(login):
    return users_repos.get(login)