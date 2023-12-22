def roman_rec(num:int)->str:
    assert isinstance(num, (str, int))
    if isinstance(num, int): num = str(num)

    d = {1000: "M", 100:"C", 10:"X", 1:"I"}
    d_full = {1000: "M", 500:"D", 100:"C", 50:"L", 10:"X", 5:"V", 1:"I"}
    lst = [val for val in d_full.values()][::-1]
    
    



    pass
