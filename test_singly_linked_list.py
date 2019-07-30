# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:30:50 2019

@author: pc
"""

'''
新建单链表Node节点类
'''
class Node():
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next      
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next
    def set_value(self, value):
        self.value = value
    def set_next(self, next):
        self.next = next

'''
新建一个链表类
'''
class LinkList():
    def __init__(self):
        # 初始化链表头结点以及链表的长度
        self.head = Node()
        self.length = 0
    def isEmpty(self):
        return self.length == 0
    def append(self, value):
        '''
            链表末尾插入节点
            * 判断是否为空链表
                * 空链表则头结点指向该节点，length加一
                * 非空链表则插入节点到最后一个，length加一
        '''
        node = Node(value)
        if self.length == 0:
            self.head.next = node
            self.length += 1
        else:
            tempNode = self.head.next
            while tempNode.next:
                tempNode = tempNode.next
            tempNode.next = node
            self.length += 1
    def len(self):
        return self.length
    
    def remove(self, index):
        '''
            * 判断链表是否为空
            * 判断删除的是否为头结点
            * 判断删除的长度是否合法
            * 找到要删除的节点的前一个节点，然后将该节点的下一个指针指向要删除的节点的下一个节点
            * 删除节点后length减一
        '''
        if self.isEmpty():
            print('This LinkList Is Empty...')
        elif (index <= 0 or index > self.length):
            print('Error Length...')
        elif index == 1:
            p = self.head.next
            self.head = p
            self.length -= 1
        else:
            p = self.head.next
            for i in range(2, index):
                p = p.next
            q = p.next
            p.next = q.next
            self.length -= 1
    
    def update(self, index, value):
        '''
            * 判断链表是否为空
            * 判断index是否合法
            * 找到待修改节点，修改其value值
        '''
        if self.isEmpty():
            print('This LinkList Is Empty...')
        elif (index <= 0 or index > self.length):
            print('Error Length...')
        else:
            p = self.head.next
            for i in range(1, index):
                p = p.next
            p.value = value
    def search(self, value):
        '''
            * 判断链表是否为空
            * 遍历链表查找节点是否存在
        '''
        if self.isEmpty():
            print('This LinkList Is Empty...')
        else:
            p = self.head.next
            for i in range(1, self.length + 1):
                if p.value == value:
                    print('Search Success!')
                    break
                elif i == self.length and p.value != value:
                    print('Search Faild!')
                else:
                    p = p.next
            
        
        
head = None
for i in range(6):
    head = Node(i,head)
while head != None:
    print(head.value) # 输出：5,4,3,2,1,0
    head = head.next

l = LinkList()
l.append(2)
l.append(3)
l.append(8)
print('链表长度:',l.len())
i=1
tempNode = l.head.next
while tempNode != None:
    print('第%d个链表节点的值:%d'%(i, tempNode.value))
    tempNode = tempNode.next
    i += 1
    
l.update(3,5)
l.update(-1,5)
l.search(10)