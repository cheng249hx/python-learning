from abc import ABC, abstractmethod
import json

#定义图书类
class Book:
    def __init__(self,book_id,book_title,author,total_copies):
        self.book_id = book_id                      #书籍编号
        self.book_title = book_title                #书名
        self.author = author                        #书籍作者m
        self.total_copies= total_copies                   #书籍总数
        self.__available_sum = total_copies            #书籍可借阅数量

    def borrow_book(self):                          #借书
        if self.__available_sum > 0:
            self.__available_sum -= 1
            return True
        else:
            return False

    def return_book(self):                          #还书
        self.__available_sum += 1

    def get_available_num(self):                    #获取书籍的可借阅数量
        return self.__available_sum

#定义会员类
class Member(ABC):
    def __init__(self,member_id,member_name,password):
        self.member_id = member_id                  #会员编号
        self.member_name = member_name              #会员姓名
        self.__password = password                  #会员密码
        self.__borrow_books = []                    #会员借阅列表

    @abstractmethod
    def get_max_sum(self)->int:                     #获取会员最大借阅量
        pass

    def borrow_book(self,book: Book):                #借书
        #判断借阅量是否达到上限
        if len(self.__borrow_books) >= self.get_max_sum():
            print(f"借阅失败，您最多可借阅{self.get_max_sum()}本书籍")
            return False

        #判断图书是否可节约
        if book.borrow_book():
            self.__borrow_books.append(book)
            print(f"{self.member_name}成功借阅{book.book_title}!")
            return True
        else:
            print(f"借阅失败，{book.book_title}可借阅数量不足！")
            return False

    def return_book(self,book: Book):               #还书
        #判断会员是否借阅了该书籍
        if book in self.__borrow_books:
            self.__borrow_books.remove(book)        #会员还书
            book.return_book()                      #图书可借阅数量+1
            print(f"{self.member_name}归还书籍{book.book_title}!")
        else:
            print(f"{self.member_name}未借阅该书籍。")

    def get_password(self):                         #获取会员密码
        return self.__password

    def get_borrow_books(self):                     #获取会员借阅列表
        return self.__borrow_books

#定义普通会员类
class VIP(Member):
    def get_max_sum(self)->int:                     #获取会员最大借阅量
        return 3

#定义超级会员类
class SVIP(Member):
    def __init__(self,member_id,member_name,password,svip_lv):
        Member.__init__(self,member_id,member_name,password)
        self.SVIP_lv = svip_lv

    def get_max_sum(self) -> int:  # 获取会员最大借阅量
        return 6 + self.SVIP_lv

#图书管理系统
class LibrarySystem:
    def __init__(self):
        self.books = {}                             #{编号1：Book对象1，编号2：Book对象2，…………}
        self.members = {}                           #{会员id：Member对象，…………}
        self.current_member: Member|None = None     #记录当前登录的会员
        #加载数据
        self.load_books_data()
        self.load_members_data()

    def load_books_data(self):
        with open("books.json","r",encoding="utf-8") as f:
            book_data = json.load(f)
            for book in book_data:
                self.books[book["book_id"]] = Book(book["book_id"],book["title"],book["author"],book["total_copies"])
            print("书籍信息加载完成。")

    def load_members_data(self):
        with open("members.json","r",encoding="utf-8") as f:
            member_data = json.load(f)
            for member in member_data:
                #判断会员类型
                if member["会员卡号"].startswith("N"):
                    self.members[member["会员卡号"]] = VIP(member["会员卡号"],member["会员姓名"],member["会员密码"])
                elif member["会员卡号"].startswith("V"):
                    self.members[member["会员卡号"]] = SVIP(member["会员卡号"], member["会员姓名"], member["会员密码"],member["会员等级"])
            print("会员信息加载完成。")

    def login(self):
        while True:
            print("【登录】")
            member_id = input("请输入账号：")
            password =  input("请输入密码")
            if member_id not in self.members:
                print("账户不存在，请重新输入！")
                continue

            #判读密码是否正确
            member = self.members[member_id]
            #密码是一个私密属性，类外无法直接访问
            if password == member.get_password():
                print(f"登录成功，欢迎{member.member_name}")
                #更改当前登录的会员
                self.current_member = member
                return True
            else:
                print("密码错误！")
                continue

    def borrow_book(self):
        #加载图书信息
        for book in self.books.values():
            print(f"编号{book.book_id:-<10}书名:《{book.book_title}》，{"-":-^20}作者:{book.author:-<15}，总数{book.total_copies}，剩余{book.get_available_num()}")
        #接受图书编号
        book_id = input("请输入要借阅的图书的编号：")
        if book_id not in self.books:
            print("借阅失败，图书不存在！")
            return

        self.current_member.borrow_book(self.books[book_id])
        #Book对象的借书行为在上述方法中以被调用，此处不用重复调用
        #self.books[book_id].borrow_book()

    def return_book(self):
        #加载借阅列表
        print("【您已借阅的数据如下：】")
        borrow_book = self.current_member.get_borrow_books()
        for book in borrow_book:
            print(f"编号{book.book_id:-<10}书名:《{book.book_title}》")

        #输入还书编号
        book_id = input("请输入归还书籍的编号：")
        if book_id not in self.books:
            print("还书失败，系统内没有该编号对应的书籍")
            return
        elif self.books[book_id] not in borrow_book:
            print("还书失败，您没有借阅该书籍。")
            return
        else:
            self.current_member.return_book(self.books[book_id])

    def show_books(self):
        print("【您已借阅的数据如下】")
        borrow_book = self.current_member.get_borrow_books()
        if len(borrow_book) > 0:
            for book in borrow_book:
                print(f"编号{book.book_id:-<10}书名:《{book.book_title}》")
        else:
            print("您没有借阅任何书籍。")

    def run(self):
        if self.login():
            while True:
                print("\n1.借阅图书")
                print("2.归还图书")
                print("3.查看借阅")
                print("4.退出")

                op = input("请选择操作（1-4）")
                match op:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.show_books()
                    case "4":
                        print("Bye~!")
                        break
                    case _:
                        print("输入有误")

if __name__ == "__main__":
    ls = LibrarySystem()
    ls.run()