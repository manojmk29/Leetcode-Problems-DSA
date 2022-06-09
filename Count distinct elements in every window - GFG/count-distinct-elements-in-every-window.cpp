// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;



 // } Driver Code Ends

class Solution{
  public:
    vector <int> countDistinct (int A[], int n, int k)
   {
       //code here.
       unordered_map<int, int> mp;
       for(int i = 0;i<k;i++)
       {
           mp[A[i]]++;
       }
       vector<int>v;
       v.push_back(mp.size());
       int i = 0,j=k-1;
       while(j<n && i<n-k)
       {
           j++;
           if(mp[A[i]]==1)
           mp.erase(A[i]);
           else
           mp[A[i]]--;
           i++;
          
           mp[A[j]]++;
           v.push_back(mp.size());
       }
       return v;
   }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {

        int n, k;
        cin >> n >> k;
        int a[n];
        for (int i = 0; i < n; i++) 
        	cin >> a[i];
        Solution obj;
        vector <int> result = obj.countDistinct(a, n, k);
        for (int i : result) 
        	cout << i << " ";
        cout << endl;
    }
    return 0;
}  // } Driver Code Ends