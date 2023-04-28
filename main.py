# This is a sample Python script.
from urllib.request import urlopen
import ijson
import time
import random
import json

class LinkedList:
    def __init__(self):
        self.head = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


f = open('default-cards.json', errors="ignore")

llist = LinkedList()
cards = 0

for card in ijson.items(f,"item"):
    if card["legalities"]["vintage"] == "leg al":
        cards += 1
        if cards == 1:
            node = Node(card)
            llist.head = node
            previous_node = node
        else:
            node = Node(card)
            previous_node.next = node
            previous_node = node
f.close()

while True:
    time.sleep(1)
    fp = open('transfer.txt', 'r+')
    line = fp.read()
    if line == "run":
        random_number = random.randrange(1, cards)
        i = 0
        random_card = llist.head
        while i < random_number:
            random_card = random_card.next
            i += 1
        fp.seek(0)
        fp.truncate()
        print(random_card.data)
        fp.write(str(random_card.data))
    fp.close()
