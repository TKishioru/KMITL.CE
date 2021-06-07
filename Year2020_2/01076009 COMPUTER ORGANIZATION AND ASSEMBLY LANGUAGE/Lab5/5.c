/*
จงพัฒนาโปรแกรมภาษา C โดยประกาศตัวแปรและตั้งค่าเริ่มต้น int i = 0 และให้วนลูปเพิ่มค่า i = i + 1 จน i มีค่าเป็นลบแล้วแสดงผลค่าของ i มาทางหน้าจอ
*/

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i = 1;
    while (i>0){
        i = i + 1;
        if(i < 0){
            printf("i was %10d before\n",i-1);
            printf("i was %10d now\n",i);
        }
    }
    return 0;
}