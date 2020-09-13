def valid(s):
    valid = True
    if len(s)%2 != 0: #since pairs of brackets required to be valid. if odd its definitely invalid
        valid = False
        return valid

    for i in range(1,len(s),2): #iterate every potential pair
        if (s[i-1] == '(' and s[i] != ')') or (s[i-1] == '{' and s[i] != '}') or (s[i-1] == '[' and s[i] != ']'):
            valid = False         
       
    return valid
    
s ='()()[]{}{}[][]()'

print(valid(s))


    
