#include <reg51.h>//头文件
/*
本模块的第九脚也就是RX脚连接到单片机的P3^1
        第十脚也就是TX脚连接到单片机的P3^0(如果你不处理本模块返回的数据可以不连接)
				同时本模块和单片机还要共地急GND连接GND
				本模块五伏供电也可以直接由单片机上的电源供电
*/

typedef   unsigned char  uint8;
typedef   unsigned int   uint16;
sbit KEY1=P3^4;//第一曲键
sbit KEY2=P3^5;//下一曲键
sbit KEY3=P3^6;//音量+键
sbit KEY4=P3^7;//音量减键


uint8 First[]={0x7E,0x04,0x03,0x00,0X01,0xEF};//第一曲指令
uint8 Next[]={0x7E,0x02,0x01,0xEF};    				//下一曲指令
uint8 Add[]={0x7E ,0x02, 0x04, 0xEF};					//音量+指令	
uint8 Sub[]={0x7E ,0x02 ,0x05, 0xEF};         //音量减指令

/*
 * UART初始化
 * 波特率：9600
*/
void UART_init(void)
{
    SCON = 0x50;        // 10位uart，允许串行接受

    TMOD = 0x20;        // 定时器1工作在方式2（自动重装）
    TH1 = 0xFD;
    TL1 = 0xFD;         //设置波特率为9600

    TR1 = 1;
}

/*
 * UART 发送一字节
 入口参数uint8的数据类型 即要发送的数据
*/
void UART_send_byte(uint8 dat)
{
	SBUF = dat;
	while (TI == 0);
	TI = 0;
}

/*
 * UART 发送字符串 
  第一个参数要发送字符串或数据的首地址
  第二个参数是要发送的数据或字符串的长度
*/
void UART_send_string(uint8 *buf,uint8 len)
{  uint8 i;
	for(i=0;i<len;i++)
		UART_send_byte(*buf++);
}

main()
{
	UART_init();//串口初始化
	
	while (1)   //一个大循环一直在检测按键和发送指令
	{  if(KEY1==0)//如果第一个键被按下播放第一段

    {		while(!KEY1);//等待按键松开
			 UART_send_string(First,6);
    }		
		else if(KEY2==0)//如果第二个按键按下播放下一曲

    {		while(!KEY2);//等待按键松开
			 UART_send_string(Next,4);
    }		
		else if(KEY3==0)//如果第三个按键按下音量加
			{		while(!KEY3);//等待按键松开
			 UART_send_string(Add,4);
    }	
 else if(KEY4==0)//如果第四个按键按下音量减

    {		while(!KEY4);//等待按键松开
			 UART_send_string(Sub,4);
    }			
	}

}