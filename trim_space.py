# -*- coding: utf-8 -*-

#递归方法
def trim(s):
    """去除首尾的空格"""
    if s[:1] == " ":
        return trim(s[1:])
    if s[-1:] == " ":
        return trim(s[:-1])
    return s

str1 = trim("  hello world!    ")
print(str1)