'''
Created on 2019年7月18日

@author: qiao.gu
'''
from sys import argv
from os.path import exists
from asn1crypto._ffi import null
# from past.builtins.misc import raw_input

# Test01
# first, second, third = argv
# 
# print('1: ', first)
# print('2: ', second)
# print('3: ', third)

# Test02
# prompt = ">"
# username = raw_input("what's your name:----")
# print(prompt)
# print(username)
# print(prompt)
# city = raw_input("Where are you living %s?" % username)
# print(prompt)
# print(city)
# print(prompt)

# # Test03
# def print_one(username, password):
#     if username != 0:
#         print(username)
#     else:
#         print("=========")
# print_one(1,20)

# # Test04
# def test01():
#     count1 = ['APPLE','ORANGE','BANANA','PAY','GOOD','BAD','NOTABILITY']
#     for i in range(0,5):
#         print("This is count %s" % count1[i])
# test01()

# # 字典 & 列表
# thing = ['a','b','c','d','e']
# charctor = {'A':'APPLE','B':'BOOK','C':'CAT','D':'DOG','E':'EGG','F':'FRUIT'}
# print(thing)
# print(thing[1])
# print(charctor['A'])
# print(charctor)

# # Class类
# class function(object):
#     def print_zd(self):
#         thing = ['a','b','c','d','e']
#         print(thing)
#         print(thing[1])
#     def print_lb(self):
#         charctor = {'A':'APPLE','B':'BOOK','C':'CAT','D':'DOG','E':'EGG','F':'FRUIT'}
#         print(charctor['A'])
#         print(charctor)       
# a = function()
# b = function()
# 
# a.print_lb()
# b.print_zd()

# # 新建网站，使用lpthw.web库
# import web

# # class __dict__对象使用实例
# class Item:
#     def __init__ (self, name, price):
#         self.name = name
#         self.price = price
# im = Item('鼠标', 28.9)
# print(im.__dict__)  # ①
# # 通过__dict__访问name属性
# print(im.__dict__['name'])
# # 通过__dict__访问price属性
# print(im.__dict__['price'])
# im.__dict__['name'] = '键盘'
# im.__dict__['price'] = 32.8
# print(im.name) # 键盘
# print(im.price) # 32.8

# 查看包 & 库 内容
import sys
dir(sys)