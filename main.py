import ijson
import time
import random
import json

#Linked List function comprised of Nodes
class LinkedList:
    def __init__(self):
        self.head = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Opens the json containing the cards.  Errors must be set to ignore or a UTF-8 error will result from non-english characters on the cards
f = open('default-cards.json', errors="ignore")

#create the linked list
llist = LinkedList()

#cards counts the number of cards read into the linked list
cards = 0

#for loop that runs through the JSON file opened above and creates the linked list for only vintage legal cards.
for card in ijson.items(f,"item"):
    if card["legalities"]["vintage"] == "legal":
        cards += 1
        if cards == 1: #this is the first card in the list so the card becomes the linked list head
            node = Node(card)
            llist.head = node
            previous_node = node
        else:
            node = Node(card)
            previous_node.next = node
            previous_node = node
f.close()

#starts an infinite 'while' loop.
while True:
    time.sleep(1)
    fp = open('transfer.txt', 'r+')
    line = fp.read() #reads the first line from the open text file
    if line == "run": 
        random_number = random.randrange(1, cards) #creates a random number from 1 to the number of cards in the linked list
        i = 0
        random_card = llist.head
        while i < random_number: #cycles through each card in the linked list until i is the random number.
            random_card = random_card.next
            i += 1
        fp.seek(0) #goes back to the start of the transfer.txt file
        fp.truncate() #deletes the content in the transfer.txt file
        print(random_card.data) #prints the random_card to the console (this can be removed if desired)
        fp.write(str(random_card.data)) #puts the card data into the text file as a string
    fp.close()
