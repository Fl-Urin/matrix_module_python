def ROMAN(num:int)->str:
    """
    find the roman representation of an int
    using two helper functions
    int_to_roman_dict(), dict_to_roman()
    """

    d_full = {1000: "M", 500:"D", 100:"C", 50:"L", 10:"X", 5:"V", 1:"I"}
    lst = [val for val in d_full.values()][::-1]
    base_10 = {1000: "M",100:"C", 10:"X",1:"I"}

    def int_to_roman_dict(num:int)->dict:
        """find the roman representation of any integer number"""
        assert isinstance(num, int)
        assert num != 0

        #adapt 04d and 10000 to whatever is defined
        num = f"{num:04d}" if num<10**(len(base_10)+1) else str(num)
        sol = {ro: int(num[-1*len(base_10):][idx]) for idx,ro in enumerate(base_10.values())}
        sol[lst[-1]] = int(num[:-1*len(base_10)+1])
        return sol
    
    def dict_to_roman(roman_dict: dict)->str:
        assert isinstance(roman_dict, dict)
        def find_next_in_lst(val):
            try:
                item = lst[lst.index(val)+1]
                return item
            except IndexError:
                return 
        
        roman_string = "".join(key*roman_dict[key] if 4 > roman_dict[key] or key==lst[-1] else 
                               key+find_next_in_lst(key) if 4 == roman_dict[key] else
                                key+find_next_in_lst(find_next_in_lst(key)) if 9 == roman_dict[key] else 
                               find_next_in_lst(key)+key*(roman_dict[key]-5)
                               for key in roman_dict.keys())

        return roman_string
    return dict_to_roman(int_to_roman_dict(num))