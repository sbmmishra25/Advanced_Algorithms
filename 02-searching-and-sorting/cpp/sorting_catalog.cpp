#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

void insertionSort(vector<int>& a){
    for(int i=1;i<(int)a.size();++i){int x=a[i],j=i-1;while(j>=0&&a[j]>x){a[j+1]=a[j];--j;}a[j+1]=x;}
}
void selectionSort(vector<int>& a){
    for(int i=0;i<(int)a.size();++i){int p=i;for(int j=i+1;j<(int)a.size();++j)if(a[j]<a[p])p=j;swap(a[i],a[p]);}
}
void mergeSort(vector<int>& a,int l,int r){
    if(l>=r)return;int m=l+(r-l)/2;mergeSort(a,l,m);mergeSort(a,m+1,r);
    vector<int>b;b.reserve(r-l+1);int i=l,j=m+1;
    while(i<=m&&j<=r)b.push_back(a[i]<=a[j]?a[i++]:a[j++]);
    while(i<=m)b.push_back(a[i++]);while(j<=r)b.push_back(a[j++]);
    copy(b.begin(),b.end(),a.begin()+l);
}
int partitionQS(vector<int>& a,int l,int r){
    int p=a[r],i=l;for(int j=l;j<r;++j)if(a[j]<=p)swap(a[i++],a[j]);swap(a[i],a[r]);return i;
}
void quickSort(vector<int>& a,int l,int r){if(l>=r)return;int p=partitionQS(a,l,r);quickSort(a,l,p-1);quickSort(a,p+1,r);}
void heapSort(vector<int>& a){make_heap(a.begin(),a.end());sort_heap(a.begin(),a.end());}
void print(const vector<int>& a){for(int x:a)cout<<x<<' ';cout<<'\n';}
int main(){vector<int>a={9,4,7,3,1,8,2,6,5};insertionSort(a);print(a);return 0;}
