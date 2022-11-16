#User function Template for python3

class Solution:
    def increment(self, arr, N):
        # code here
        res=0
        if(arr[-1]<9):
            arr[-1]=arr[-1]+1
            return arr
        for i in arr:
            res=res*10+i
        res+=1
        return list(str(res))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        ptr = ob.increment(arr,N)
        for i in ptr:
            print(i,end=" ")
        print()
# } Driver Code Ends
