using System;
using System.Threading;

namespace OS_Problem_02
{
    class Thread_safe_buffer
    {
        // TSBuffer [Front][][][][Back]
        //          ---- Count = n ----
        static int[] TSBuffer = new int[10]; //Same Resource
        static int Front = 0;
        static int Back = 0;
        static int Count = 0;
        private static int updateFlag = 0;
        private static Object _Lock = new object();
        
        //Function
        static void EnQueue(int eq)
        {
            TSBuffer[Back] = eq;
            Back++;
            Back %= 10;
            Count += 1;
        }

        static int DeQueue()
        {
            int x = 0;
                x = TSBuffer[Front];
                Front++;
                Front %= 10;
                Count -= 1;
         
            return x;
        }

        //EnQueue 01 011 : 1 11
        static void th01()
        {
            lock (_Lock)
                if (updateFlag == 0)
                {
                    for (int i = 1; i < 51; i++)
                    {
                        EnQueue(i);
                        Thread.Sleep(5);
                    }
                    updateFlag = 1;
                }
        }

        static void th011()
        {
            lock (_Lock)
                if (updateFlag == 0)
                {
                    for (int i = 100; i < 151; i++)
                    {
                        EnQueue(i);
                        Thread.Sleep(5);
                    }
                    updateFlag = 1;
                }
        }

        //ใช้ DeQueue 02 : 2 21 22
        static void th02(object t)
        { 
            int j;/*
           lock (_Lock)
                if (updateFlag == 1 && Count != 0)
                {*/
                    for (int i = 0; i < 60; i++)
                    {
                if (Count > 0)
                {
                    j = DeQueue();
                    Console.Write("--- {0}", Count);
                    Console.WriteLine("j={0}, thread:{1}", j, t);
                    Thread.Sleep(100);
                }
                else
                {
                    Console.WriteLine("--- Loss {0}", i);
                    //Console.WriteLine("Wait");
                    //i--;
                }
                
            }
                /*    updateFlag = 0;
                }*/
        }
        static void Main(string[] args)
        {
            Thread t1 = new Thread(th01);
            //Thread t11 = new Thread(th011);
            Thread t2 = new Thread(th02);
            //Thread t21 = new Thread(th02);
            //Thread t22 = new Thread(th02);

            t1.Start();
            //t11.Start();
            t2.Start(1);
            //t21.Start(2);
            //t22.Start(3);
        }
    }
}
