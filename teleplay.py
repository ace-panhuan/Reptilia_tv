class Teleplay:
    def __init__(self):
        self.__talename = None
        self.__director_list = None
        self.__author_list = []
        self.__score = 0
        self.__synopsis = None

    def set_name(self,n):
        self.__talename = n

    def add_director(self,d):
        self.__director_list = d

    def add_author(self,a):
        self.__author_list.append(a)

    def add_synopsis(self,c):
        self.__synopsis = c

    def set_score(self,s):
        self.__score = s


    def __repr__(self):
        author_list = "*".join(self.__author_list)
        s = "片名:{}\n导演:{}\n主演:{}\n评分:{}\n简介:{}\n".format(self.__talename,
                                                         self.__director_list,author_list,
                                                         self.__score,self.__synopsis)

        return s


