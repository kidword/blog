# -*- coding:utf-8 -*-
from spider_model.db.mydb import MySQL
from spider_model.middleware.middle import user_agent


class Spider:
    mysql = MySQL()

    def schedule(self):
        list1 = ['jav', 'klo', 'ol', 'lov', 'pop']
        for i in range(len(list1)):
            lis = {
                "name": list1[i],
                "age": "20",
                "id": int(i + 1)
            }
            self.mysql.query_insert('students', lis)

        self.mysql.db_close()


if __name__ == '__main__':
    sp = Spider()
    sp.schedule()
