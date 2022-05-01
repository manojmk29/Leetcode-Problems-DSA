class Solution:
    def canCompleteCircuit(self,gas,cost):
        n=len(gas)
        gas_tot=sum(gas)
        cost_tot=sum(cost)
        if(cost_tot>gas_tot):
            return(-1)
        start=0
        tot=0
        for i in range(n):
            tot-=cost[i]
            tot+=gas[i]
            if(tot<0):
                tot=0
                start=i+1
        return(start)
    