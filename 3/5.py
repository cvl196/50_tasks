def pluser(st):
    for i in range(1,len(st)-1):
        if st[i] != '+' and st[i+1] == '+' and st[i+1] == '+':
            return True
        else:
            return False


print(pluser('+32+3+4+2+3+4+'))