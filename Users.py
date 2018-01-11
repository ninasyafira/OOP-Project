class Users():
    def __init__(self, parent,child):
        self.__parent = parent
        self.__child = child

    def get_parent(self):
        return self.__parent
    def get_child(self):
        return self.__child

    def set_parent(self, parent):
        self.__parent = parent
    def set_child(self, child):
        self.__child = child