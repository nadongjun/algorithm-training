#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector <int> v;
    int N, M = 0;
    int result = 0;
    cin >> N >> M;
    for (int i = 0; i < N; i++)
    {
        int input;
        cin >> input;
        v.push_back(input);
    }

    for (int i = 0; i < N; i++)
    {
        for (int j = i+1; j < N; j++)
        {
            for (int k = j+1; k < N; k++)
            {
                
                if(M>=v.at(i)+v.at(j)+v.at(k) && result <= v.at(i) + v.at(j) + v.at(k))
                    result = v.at(i) + v.at(j) + v.at(k);
            }
        }
    }
    cout << result;
    return 0;
}
