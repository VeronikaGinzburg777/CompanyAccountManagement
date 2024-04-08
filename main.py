# Разработай систему управления учетными записями пользователей для небольшой
# компании. Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID),
# имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.
#
# Требования:
#
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
#
# 2.Класс Admin: Этот класс должен наследоваться от класса User.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять
# и удалять пользователей из списка (представь, что это просто список экземпляров User).
#
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации
# снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User():
    def __init__(self, id, name):
        self.__user_id = id
        self.__user_name = name
        self.__access_level = "user"

    def get_user_id(self):
        return self.__user_id
    def get_user_name(self):
        return self.__user_name

    def get_access_level(self):
        return self.__access_level

class Admin(User):
    def __init__(self, id, name):
        super().__init__(id, name)

        self.__access_level = "admin"

    def get_access_level(self):
        return self.__access_level

    def add_user(self, user_list, user):
        user_list.append(user)

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                break

user1 = User("1","Алиса")
user2 = User("2","Екатерина")
admin = Admin("3","Вероника")
print(admin.get_access_level())

user_list = [user1, user2]

admin.add_user(user_list, admin)

print("Список пользователей")

for user in user_list:
    print(f" ID: {user.get_user_id()} Имя: {user.get_user_name()} Уровень доступа: {user.get_access_level()}")

admin.remove_user(user_list, "2")

print("Обновленный список пользователей ")

for user in user_list:
    print(f" ID: {user.get_user_id()} Имя: {user.get_user_name()} Уровень доступа: {user.get_access_level()}")