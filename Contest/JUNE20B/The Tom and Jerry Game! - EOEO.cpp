#include<iostream>
using namespace std;
#define ll long long
int main()
{
ll int test;
cin >> test;
while(test--)
{
ll int Tom_s;
cin >> Tom_s;
while(Tom_s%2==0){
    Tom_s = Tom_s/2;
}
cout << (Tom_s-1)/2 << endl;

}


}