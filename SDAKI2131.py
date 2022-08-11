#Fill your identitiy here
#Nama: Arya Fakhruddin Chandra
#NPM: 2006607526
#Kode Asdos: NF
from sys import stdin
#Create a linked list using this class
#Modify this class freely to fit your code
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def remove(self, node):
        if node == None:
            return
        if self.size == 1:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
            self.head.prev = None
        elif node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            self.size -= 1
  
    def insertBefore(self, target_node, insert_node):
        if target_node == self.head:
            return self.addFirst(insert_node)
        elif target_node == None:
            return self.addLast(insert_node)
        else:
            insert_node.prev = target_node.prev
            insert_node.next = target_node
            if target_node.prev is not None:
                target_node.prev.next = insert_node
            else:
                self.head = insert_node
            target_node.prev = insert_node
            self.size += 1
            return insert_node

    def insertAfter(self, target_node, insert_node):
        if target_node == self.tail:
            return self.addLast(insert_node)
        else:
            insert_node.next = target_node.next
            insert_node.prev = target_node
        if target_node.next is not None:
            target_node.next.prev = insert_node
        else:
            self.tail = insert_node
        target_node.next = insert_node
        self.size += 1
        return insert_node

    def addFirst(self, node):
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.size += 1
        return node

    def addLast(self, node):
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1
        return node

    def print(self):
        out = ""
        cur = self.head
        while cur is not None:
            out += str(cur.data)
            cur = cur.next
        print(out)

dll = LinkedList()
dll_cursor = None
dll_ins = False
n_commands = int(stdin.readline())
for _ in range(n_commands):
    curr_command = stdin.readline().split()
    if curr_command[0] == "ADD":
        new_node = Node(curr_command[1])
        if dll.size == 0:
            dll_cursor = dll.addFirst(new_node)
            dll_cursor = dll_cursor.next
        elif dll_cursor == None:
            dll_cursor = dll.addLast(new_node)
            dll_cursor = dll_cursor.next
        elif dll_ins:       
            dll_cursor_next = dll_cursor.next
            dll.remove(dll_cursor)
            dll_cursor = dll.insertBefore(dll_cursor_next, new_node)
            dll_cursor = dll_cursor.next
        else:
            dll_cursor = dll.insertBefore(dll_cursor, new_node)
            dll_cursor = dll_cursor.next
    elif curr_command[0] == "HOME":
        dll_cursor = dll.head
    elif curr_command[0] == "END":
        dll_cursor = dll.tail
    elif curr_command[0] == "INS":
        dll_ins = not dll_ins
    elif curr_command[0] == "RIGHT":
        if dll_cursor is not None:
            dll_cursor = dll_cursor.next
    elif curr_command[0] == "LEFT":
        if dll_cursor is not None:
            dll_cursor = dll_cursor.prev
        else:
            dll_cursor = dll.tail
    elif curr_command[0] == "DEL":
        if dll_cursor == None:
            continue
        if dll.size == 1:
            dll.remove(dll_cursor)
            dll_cursor = None
        else:
            dll_cursor_next = dll_cursor.next
            dll.remove(dll_cursor)
            dll_cursor = dll_cursor_next
dll.print()
#  if dll_cursor is not None:
#    print(str(dll_cursor.data))