class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = {5:0, 10:0}
        for customer in bills:
            if customer == 5:
                register[5] += 1
            if customer == 10:
                if register[5] >= 1:
                    register[5] -= 1
                    register[10] += 1
                else:
                    return False
            if customer == 20:
                if register[10] >= 1 and register[5] >= 1:
                    register[10] -= 1
                    register[5] -= 1
                elif register[5] >= 3:
                    register[5] -= 3
                else:
                    return False
        return True



"""
bills = [5,10,5,5,20]
register = {5:2, 10:0}


"""
        