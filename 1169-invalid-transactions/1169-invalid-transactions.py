class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        n=len(transactions)
        name=[]
        time=[]
        amount=[]
        place=[]
        for i in range(n):
            arr=transactions[i].split(",")
            name.append(arr[0])
            time.append(arr[1])
            amount.append(arr[2])
            place.append(arr[3])
        ret=[]
        ind=set()
        for i in range(n):
            if(int(amount[i])>=1000 and i not in ind):
                ret.append(",".join([name[i],time[i],amount[i],place[i]]))
                ind.add(i)
            for j in range(n):
                if(j!=i):
                    if(name[i]==name[j] and place[i]!=place[j] and int(time[j])<=int(time[i])+60 and int(time[j])>=int(time[i])-60):
                        if j not in ind:
                            ret.append(",".join([name[j],time[j],amount[j],place[j]]))
                            ind.add(j)
                        if(i not in ind):
                            ret.append(",".join([name[i],time[i],amount[i],place[i]]))
                            ind.add(i)
        return(ret)