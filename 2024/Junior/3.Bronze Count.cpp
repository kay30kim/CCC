#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set> // set -> index로 접근이 불가능하다! 37번째줄..!
//implicit declaration of function 'sort' 
// 함수를 명시적으로 선언 않은 채 사용 

// arr 1 - award - 점수를 보관하는데 중복 계산 x 70 70 72 => arr1 => [72, 70]
// arr 2  - 같은 점수를 받은 사람의 수를 나타내는 배열  ex) arr[70] = 3 -> 70점인 사람이 3명이다
using namespace std;

int main()
{
    int participants = 0;
    int score = 0;
    set<int> award;
    vector<int> arr2(76, 0);
    //int arr2[76]; //Each score is between 0 and 75 (inclusive)
    int i = 0;

    scanf("%d", &participants); // 3 
    //vector<Node> arr(participants, {0, 0}); // [ {0, 0}, {0, 0}. {0, 0} ]

    for (; i < participants; i++)
    {
        int num;
        scanf("%d", &num); // 0번째 위치에 들어감
        award.insert(num);
        arr2[num] += 1;
        // 1) for 문 -> award[i] 0~i-1 같은게 있는지 확인후 -> 같은 게 있으면 추가 안하고, 같은게 없으 면 추가
        // 2) sort -> binary search -> O(NlogN) + O(logN) => O(NlogN)
        // 3) set -> O(1)
    }
    // 정렬하는 방법 (vector, array, set)
    // sort(award.begin(),award.end()); vector 정렬 
    // std::sort(award, award + participants); // 시작주소, 끝주소
    // // sort(award.begin(), award.end()); -> set정렬

  /* vector는 가능한 풀이, 하지만 set은 이렇게 출력 불가능 / array -> sizeof(array) / sizeof(int)
    for (int i = 0; i < award.size(); i++)
    {
        printf("%d ", award[i]);
    }
    printf("\n");
  */

    int idx = 1;
    //for (auto& num : award) { // asending order
    for (auto it = award.rbegin(); it != award.rend(); ++it) {
        if (idx == 3) { // desending order
            printf("%d %d", *it, arr2[*it]);
        }
        idx += 1;
    }
    printf("\n");
    return 0;
}