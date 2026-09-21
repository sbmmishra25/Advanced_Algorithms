#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
int linearSearch(const vector<int>&a,int x){for(int i=0;i<(int)a.size();++i)if(a[i]==x)return i;return -1;}
int binarySearch(const vector<int>&a,int x){int l=0,r=(int)a.size()-1;while(l<=r){int m=l+(r-l)/2;if(a[m]==x)return m;if(a[m]<x)l=m+1;else r=m-1;}return -1;}
int lowerBound(const vector<int>&a,int x){return lower_bound(a.begin(),a.end(),x)-a.begin();}
int upperBound(const vector<int>&a,int x){return upper_bound(a.begin(),a.end(),x)-a.begin();}
int quickselect(vector<int>a,int k){nth_element(a.begin(),a.begin()+k,a.end());return a[k];}
int main(){vector<int>a={1,3,3,5,8,13};cout<<binarySearch(a,8)<<' '<<lowerBound(a,3)<<'\n';}
