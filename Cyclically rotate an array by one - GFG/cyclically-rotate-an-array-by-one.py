#User function Template for python3

def rotate( arr, n):
    def reverse(l,r):
        while(l<r):
            arr[l],arr[r]=arr[r],arr[l]
            l+=1
            r-=1
    reverse(0,n-2)
    reverse(n-1,n-1)
    reverse(0,n-1)
    
    # reverse(0,n-1)
    # reverse(1,n-1)
    # return(arr)
    
    # 1 2 3 4 5
    # 5 4 3 2 1
    # 5 1 2 3 4
    # 5 1 2 3 4
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        rotate(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends