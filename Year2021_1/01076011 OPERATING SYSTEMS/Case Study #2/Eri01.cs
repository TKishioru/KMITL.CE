
using System.Threading;
using System;
namespace ThreadingDemo
{
    class Program
    {
        private static object shared_resource = new object();
        private static object shared_back_index = new object();
        private static object prevT1Thread = new object();
        static int size = 10;

        static int[] TSBuffer = new int[10];
        static int Front = 0;
        static int Back = 0;
        static int Count = 0;

        static int T1_onWait = 0;
		static int T2_onWait = 0;
		static int updateFlag = 0;

		static int currentT1A = 1;
		static int currentT1B = 100;
		static int currentT2 = 0;

        static void Main(string[] args)
        {
            Thread t1 = new Thread(T1A);
            Thread t2 = new Thread(T1A);
            Thread t3 = new Thread(T1B);
            Thread t4 = new Thread(T2);
            Thread t5 = new Thread(T2);
            Thread t6 = new Thread(T2);

            t1.Start(1);
            t2.Start(2);
            t3.Start(3);
            t4.Start(4);
            t5.Start(5);
            t6.Start(6);

            t1.Join();
            t2.Join();
            t3.Join();
            t4.Join();
            t5.Join();
            t6.Join();

            Console.Read();
        }

        static void T1A(object t)
        {
			
			for (int i = 1; i < 51; i++)
            {
				lock (shared_resource)
				{
					if(currentT2>=60){
						break;
					}
					i = currentT1A;
					if(T1_onWait==0)
					{
						Thread.Sleep(5);
						if (Count < size)
						{
							enQ(i, t);
							currentT1A++;
						}
						else
						{
							Console.WriteLine("Queue is full, waiting..");
							T1_onWait = 1;
						}
					}
				}
				
            }
        }

        static void T1B(object t)
        {
            for (int i = 100; i < 151; i++)
            {
				lock (shared_resource)
				{
					if(currentT2>=60){
						break;
					}
					i = currentT1B;
					if(T1_onWait==0)
					{
						Thread.Sleep(5);
						if (Count < size)
						{
							enQ(i, t);
							currentT1B++;
						}
						else
						{
							Console.WriteLine("Queue is full, waiting..");
							T1_onWait = 1;
						}
					}
				}
				
            }
        }

        static void T2(object t)
		{
            for (int i = 0; i < 60; i++)
            {
				lock (shared_resource)
				{
					if(currentT2>=60){
						break;
					}
					i = currentT2;
					if (T2_onWait == 0)
					{
						Thread.Sleep(100);
						if (Count > 0)
						{
							deQ(t);
							T2_onWait = 0;
							currentT2++;
						}
						else 
						{
							Console.WriteLine("Count = "+Count+", Queue is empty, waiting..");
							T2_onWait = 1;
						}
					}
				}
				
            }
        }

        static void enQ(int num, object t)
        {
				TSBuffer[Back] = num;
				Back++;
				Back %= 10;
				Count += 1;
				T2_onWait = 0;
        }

        static void deQ(object t)
        {
            int x = TSBuffer[Front];
			TSBuffer[Front] = 0;
            Front++;
            Front %= 10;
            Count -= 1;

			T1_onWait = 0;

            if(currentT2<60) {
				Console.WriteLine("DeQ : " + x + " | Thread : " + t);
				Console.WriteLine("Data : [" + TSBuffer[0]+" "+ TSBuffer[1]+" "+ TSBuffer[2]+" "+ TSBuffer[3]+" "+ TSBuffer[4]+" "+ TSBuffer[5]+" "+ TSBuffer[6]+" "+ TSBuffer[7]+" "+ TSBuffer[8]+" "+ TSBuffer[9]+"]\n");
			}
        }

		
    }

	
}

//TA = 0,TB = 0,iA1 = 1,iA2 = 100,iB = 0
//Console.WriteLine("TA1 " + i + "| Thread : "+t+" Data : [" + TSBuffer[0]+" "+ TSBuffer[1]+" "+ TSBuffer[2]+" "+ TSBuffer[3]+" "+ TSBuffer[4]+" "+ TSBuffer[5]+" "+ TSBuffer[6]+" "+ TSBuffer[7]+" "+ TSBuffer[8]+" "+ TSBuffer[9]+"]\n");