# -*- coding:utf-8 -*-
"""
作者：ryangyan
日期：2021年07月06日
用途：
"""
import threading

lock = threading.Lock()

class Account:
    def __init__(self, balance):
        self.balance = balance


def draw(account, amount):
    with lock:
        if account.balance >= amount:
            print(threading.current_thread().name,
                  "取钱成功")
            account.balance -= amount
            print(threading.current_thread().name,
                  "余额", account.balance)
        else:
            print(threading.current_thread().name,
                  "取钱失败，余额不足")


if __name__ == "__main__":
    account = Account(1000)
    ta = threading.Thread(name="ta", target=draw, args=(account, 800))
    tb = threading.Thread(name="tb", target=draw, args=(account, 800))
    ta.start()
    tb.start()
