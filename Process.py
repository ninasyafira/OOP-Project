from Users import Users


def processUser():
    usersList = []
    user_file = open('file/users.txt', 'r')
    for ulist in user_file:
        list = ulist.split(',')
        s = Users(list[0],list[1])

        usersList.append(s)
    return usersList