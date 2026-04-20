/*cycle의 첫글자를 text에서 찾고
찾은 index 주위를 순회하여
cycle의 변형이 있는지 확인*/

#include<stdio.h>
int main(){
    char cycle[1001], text[1001];
    scanf("%s %s", text, cycle);
    int cycle_len=0;
    while (cycle[cycle_len]!=NULL){
        cycle_len++;
      }
  //printf("cycle_len: %d\n", cycle_len);
    
    int suc = 0; // 0==false, 1==true
    for (int i=0; i<1000; i++){ // arr[1000]은 null이므로 찾을 필요 없음
        if (text[i]==cycle[0]){
            int ip=0;
            while (i+(ip+1)<1000 && text[i+(ip+1)]==cycle[ip+1]) ip++;
            int i2=i-cycle_len;
            //if (i2<0) continue;
            while (i2+(ip+1)<1000 && text[i2+(ip+1)]==cycle[ip+1]) ip++;
            //printf("i=%d ip=%d i2=%d\n", i, ip, i2);
            if (ip+1==cycle_len){
                suc = 1;
                break;
            }
        } if(text[i]==NULL) break;
    }
    
    if (suc==1) printf("yes\n"); //있음
    else printf("no\n"); //없음
    
    return 0;
}