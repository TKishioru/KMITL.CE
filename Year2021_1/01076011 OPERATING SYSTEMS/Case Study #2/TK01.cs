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
        private static int updateFlagEn = 0;
        private static int updateFlagDe = 0;
        private static Object _LockEn = new object();
        private static Object _LockDe = new object();

        //Function
        static void EnQueue(int eq)
        {
            lock (_LockEn)
            {
                TSBuffer[Back] = eq;
                Back++;
                Back %= 10;
                Count += 1;
                //Console.WriteLine("At count {0} [Data real : {1}]", Count, eq);
            }
        }

        static int DeQueue()
        {
            lock (_LockDe) {
                int x = 0;
                x = TSBuffer[Front];
                Front++;
                Front %= 10;
                Count -= 1;
            }
            return x;
        }

        //EnQueue 01 011 : 1 11
        static void th01()
        {
            if (updateFlagEn == 0)
            {
                for (int i = 1; i < 51; i++)
                {
                    EnQueue(i);
                    Thread.Sleep(5);
                }
                updateFlagEn = 1;
            }
        }
        static void th011()
        {
            if (updateFlagEn == 0)
            {
                for (int i = 100; i < 151; i++)
                {
                    EnQueue(i);
                    Thread.Sleep(5);
                }
                updateFlagEn = 1;
            }
        }

        //DeQueue 02 : 2 21 22
        static void th02(object t)
        {
            int j;

            if (updateFlagDe == 1 && Count != 0)
            {
                for (int i = 0; i < 60; i++)
                {
                    while (Count <= 0)
                    {
                        Console.WriteLine("Wait");
                    }
                    j = DeQueue();
                    Console.Write("--- {0}", Count);
                    Console.WriteLine("j={0}, thread:{1}", j, t);
                    Thread.Sleep(100);
                }
                updateFlagDe = 0;
            }
        }
        static void Main(string[] args)
        {
            Thread t1 = new Thread(th01);
            Thread t11 = new Thread(th011);
            Thread t2 = new Thread(th02);
            //Thread t21 = new Thread(th02);
            //Thread t22 = new Thread(th02);

            t1.Start();
            t11.Start();
            t2.Start(1);
            //t21.Start(2);
            //t22.Start(3);
        }
    }
}
