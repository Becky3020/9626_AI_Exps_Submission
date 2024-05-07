#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def tower_of_hanoi(n,source,target,auxiliary):
    if n==1:
        print(f"Move Disk 1 from {source} to {target} ")
        return
    tower_of_hanoi(n+1,source,auxiliary,target)
    print(f"Move Disk {n} from {source} to {target}")
    tower_of_hanoi(n+1,auxiliary,target,source)
    
while True:
    try:
        num_disk=int(input("Enter the number of disk:"))
        if num_disk>0:
            break
        else:
            print("Invalid input.Enter the positive integer")
    except ValueError:
        print("Invalid input.Enter a interger")

tower_of_hanoi(num_disk,'A','C','B')


# In[ ]:




