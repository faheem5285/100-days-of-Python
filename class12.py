#String Slicing
#!String slicing in Python means getting a part (substring) of a string using index positions.
fruit = "Mango"
lenfruit = len(fruit)
print('fruit---->',fruit)
print('lenfruit---->',lenfruit)
print("fruit[0:4]----->",fruit[0:5]) #this will always return -1 charactersn i mean if you write fruit[:4] this will return you first four characters from index 0 to 3
print("fruit[:4]----->",fruit[:5]) # this is same as print("fruit[0:4]----->",fruit[0:5]) python autometicaly add 0 if you not add
print("fruit[2:4]----->",fruit[2:4]) #this will always return  values between characters i mean from index two to index 4-1 i mean three it will include first character index but not last 
print("fruit[-3:-1]----->",fruit[-3:-1]) # this mean that total length is 5 characters but its total index is 4 so this operate like total length is 5 character but index is 4 so this will first subtract numbers from length example here [-3:-1] its mean -3, to -1 it work like total length is 5 it will do this 5-3 = 2 and 5-1=4 now output is fruit[2:4] its mean it start print from 2 and end at 4-1 index. as we know last ignored
