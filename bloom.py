
import mmh3
import math

file1 = open('books.txt', 'r')
file2 = open('data.txt', 'r')

books_lst = file1.readlines()
data_lst = file2.readlines()

books = []
data = []

for i in books_lst:
    books.append(i.strip())
for j in data_lst:
    data.append(j.strip())
#print(data)

i=0
info=[]
while i<len(data):
  info.append(data[i:i+3])
  i+=3
  
    
def bit_array(n):  #returns bit array size
    
    bin_array = [0] * (int((2 * n)/math.log(2))) #2 number 0f hash functions
    return bin_array

def add(lines):
    bin_array = bit_array(52)
    for i in lines: 
        index1 = mmh3.hash(i) % len(bin_array)
        index2 = hash(i) % len(bin_array)
        bin_array[index1] = 1
        bin_array[index2] = 1
    return bin_array
    
        
#add(books)

def bloom(obj):
    bin_array = add(books)
    in1 = mmh3.hash(obj) % len(bin_array)
    in2 = hash(obj) % len(bin_array)
    if bin_array[in1]==1 & bin_array[in2]==1:
        return True
    else: return False
    
def Book_details(obj):
    if (bloom(obj)):
        index_book =  books.index(obj)
        author =   info[index_book][0]
        ratings = info[index_book][1]
        genre = info[index_book][2]
        new = []
        for i in range(len(books_lst)):
            if info[index_book][2] == info[i][2]:
                new.append(books[i])
        similar = ""
        for i in range(1, len(new)):
            similar+= str(i)+". "+new[i]+"\n"
    
        out = ("You have read this book. \nBook's Title: " + obj + "\nThe author of this book is: " + author + "\nYour Rating: " + ratings + "\nThe Genre is: " + genre ) 
    else: 
        similar = "   No books found :("
        out = ("Book's Title: "+ obj +"\nYou have not read this book.")
    
    return out,"Similar Books are:\n"+similar

#Book_details("Harry Potter")