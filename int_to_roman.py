def ROMAN(num:int)->str:
    """
    find the roman representation of an int
    using two helper functions
    int_to_roman_dict(), dict_to_roman()
    """

    d = {1000: "M", 100:"C", 10:"X", 1:"I"}
    d_full = {1000: "M", 500:"D", 100:"C", 50:"L", 10:"X", 5:"V", 1:"I"}
    lst = [val for val in d_full.values()][::-1]

    def int_to_roman_dict(num:int)->dict:
        """find the roman representation of any integer number"""
        assert isinstance(num, int)
        assert num != 0

        def find_biggest_below(num:int)->int:
            """
            find the largest number that is representable in the roman number system
            {1000: "M", 500:"D", 100:"C", 50:"L", 10:"X", 5:"V", 1:"I"}
            """
            return max(val for val in set(d.keys()) if num>=val)

        sol = {ro: 0 for ro in d.values()}
        while num > 0:
            roman = find_biggest_below(num)
            num = num - roman
            sol[d[roman]] += 1
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

print(ROMAN(99))
