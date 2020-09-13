def happy(num,done):
        if int(num) == 1:
            return True #if the previous number is 1
        else:
            new_num = 0            
            for i in range(0,len(num)):
                new_num += (int(num[i]))**2 #sum up squares of digits
            num = str(new_num)
            if num in done: #check if this was a number previously calculated
                return False 
            else:
                done += [num] #add number to list
                return happy(num,done) #call function to check if its happy 
            print(done)
print(happy('19',[]))

