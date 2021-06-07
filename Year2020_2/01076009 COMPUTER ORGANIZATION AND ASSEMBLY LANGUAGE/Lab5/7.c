/*
จงพัฒนาโปรแกรมภาษา C ให้สามารถอ่านไฟล์ Makefile เพื่อแสดงตัวอักษรในไฟล์ทีละตัวและค่ารหัส ASCII ฐานสิบหกของตัวอักษรนั้นบนหน้าจอ แล้วปิดไฟล์เมื่อเสร็จสิ้น
*/

//Code by Erika
#include <stdio.h>
void str2hex(char dec)
{
    int hex[100];
    int i = 0, j;

    //printf("Input Decimal value : ");
    do
    {
        hex[i] = dec % 16;
        dec /= 16;
        i++;
    } while (dec > 0);

    for (j = i - 1; j >= 0; j--)
    {
        switch (hex[j])
        {
        case 15:
            printf("F");
            break;
        case 14:
            printf("E");
            break;
        case 13:
            printf("D");
            break;
        case 12:
            printf("C");
            break;
        case 11:
            printf("B");
            break;
        case 10:
            printf("A");
            break;
        default:
            printf("%d", hex[j]);
        }
    }
}

int main()
{
    FILE *fp;
    char ch;
    char filename[255] = "makefile";
    fp = fopen(filename, "r");
    while ((ch = fgetc(fp)) != EOF)
    {
        printf("\n\'%c\':", ch);
        str2hex(ch);
    }
    return 0;
}