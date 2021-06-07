/*
จงพัฒนาโปรแกรมภาษา C โดยประกาศตัวแปรและตั้งค่าเริ่มต้น unsigned int i = 1 และให้วนลูปเพิ่มค่า i = i + 1 จน i มีค่าเป็นศูนย์แล้วแสดงผลค่าของ i มาทางหน้าจอ
*/

//Code by Aj.Surin
#include <stdio.h>
#include <stdlib.h>

int main()
{
    unsigned int i = 1;
    while (i>0){
        i = i + 1;
        if(i == 0){
            printf("i was %10u before\n",i-1);
            printf("i was %10u now\n",i);
        }
    }
    return 0;
}