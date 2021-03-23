class Case:
    def __init__(self,numHouses,budget,A_list):
        self.numHouses= numHouses
        self.budget = budget
        self.A_list = A_list
        self.maxHouses = 0
        
    def find_maxHouses(self):
        self.A_list.sort()
        curr_budget = self.budget
        for Ai in self.A_list:
            if Ai <= curr_budget:
                curr_budget -= Ai
                self.maxHouses +=1
            if curr_budget <=0:
                break
    
        return self.maxHouses



T = int(input()) # num of cases
for i in range(1,T+1):
    N, B = [int(a) for a in input().split()]
    A_list = [int(a) for a in input().split()]
    case = Case(N,B,A_list)
    print("Case #{}: {}".format(i,case.find_maxHouses()))
    