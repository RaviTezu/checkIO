#!/usr/bin/python

def checkio(capacity, number):
    nums = [str(x) for x in range(0,number)]
    str1 = "".join(nums)
    #print nums
    strs = ["".join(nums[i:i+capacity]) for i in range(0, number, capacity)]
    ret_str = ""
    if number%capacity and capacity < number:
        #print strs
        bl = strs[-2]
        for s in strs[:-1]:
            if s!= bl:
                ret_str += (s+",")*2
            else:
                ret_str = ret_str + bl + "," + bl[len(strs[-1]):] + strs[-1] + ","+ strs[-1] + bl[:len(strs[-1])]
                #ret_str = ret_str + bl + "," + bl[1:] + strs[-1][0] + "," + strs[-1]+bl[0]
    else:
        for s in strs:
            ret_str += (s+",")*2
    fn_str = ret_str.strip(",")
    #print fn_str
    for x in fn_str:
        if fn_str.count(x) == 2 or x==",":
            pass
        else:
           fn_str = fn_str+","+x
    #print fn_str
    return fn_str
    


if __name__ == '__main__':
    #This part is using only for self-checking and not necessary for auto-testing
    def check_solution(func, k, n, max_steps):
        result = func(k, n)
        actions = result.split(",")
        if len(actions) > max_steps:
            print("It can be shorter.")
            return False
        details = [0] * n
        for act in actions:
            if len(act) > k:
                print("The system can contain {0} detail(s).".format(k))
                return False
            if len(set(act)) < len(act):
                print("You can not place one detail twice in one load")
                return False
            for ch in act:
                details[int(ch)] += 1
        if any(d < 2 for d in details):
            print("I see no painted details.")
            return False
        if any(d > 2 for d in details):
            print("I see over painted details.")
            return False
        return True
    
    assert check_solution(checkio, 2, 3, 3), "1st Example"
    assert check_solution(checkio, 6, 3, 2), "2nd Example"
    assert check_solution(checkio, 3, 6, 4), "3rd Example"
    assert check_solution(checkio, 1, 4, 8), "4th Example"
    assert check_solution(checkio, 2, 5, 5), "5th Example"
    checkio(3,4)
    checkio(4,6)
       
