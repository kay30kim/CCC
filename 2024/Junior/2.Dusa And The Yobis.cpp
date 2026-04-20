
#include <stdio.h>


int main()
{
    int DusaSize;
    int Yobi;

    scanf("%d", &DusaSize);
    while(scanf("%d", &Yobi) != EOF) // 입력이 있으면 진입.
    {
        if(DusaSize > Yobi)
        {
            DusaSize += Yobi;
        }
        else
        {
            break;
        }

    }
    printf("%d", DusaSize);
}
