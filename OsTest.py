# -*- coding: utf-8 -*-
import linecache

def get_content(path):
    content=''
    data=linecache.getlines(path)
    for line in range(len(data)):
        content+=data[line]
    return content
def main():
    path='D:\\aa.txt'
    con=get_content(path)
    print con

if __name__ == '__main__':
    main()