import os

output = 'books'

if not os.path.exists(output):
    os.makedirs(output)
    
lines = open('pg10.txt','r').readlines()


books = []
books_idx = []