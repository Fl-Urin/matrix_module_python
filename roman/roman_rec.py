def roman_rec(num:int, depth=0)->str:
    assert isinstance(num, (str, int))
    #flip the number if the funciton is called the first time
    #in recursive calls the number will be string already
    if isinstance(num, int): assert num != 0; num = str(num)[::-1]

    d = ("I","V","X","L","C","D","M")

    def func(val):
        val = int(val)
        if val < 4: return val*d[depth]
        if val == 4: return d[depth]+d[depth+1]
        if val < 9: return d[depth+1]+(val-5)*d[depth]
        if val == 9: return d[depth]+d[depth+2]
    
    #BASECASE:
    if len(num) == 1 or d[depth] == d[-1]:
        if d[depth] != d[-1]:return func(num)
        if d[depth] == d[-1]:return int(num)*d[depth]

    #recursive calls
    else: return roman_rec(num[1:],depth+2)+func(num[0])