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
        private static int n = 0;
        private static object _Lock = new object();

        static void EnQueue(int eq)
        {
            lock (_Lock)
            {
                while (Count >= 10)
                {
                    Monitor.Wait(_Lock);
                    Console.WriteLine("Wait! : Full stack");
                }
                TSBuffer[Back] = eq;
                Back++;
                Back %= 10;
                Count += 1;
                //Console.WriteLine("{0} : Count{1}", eq, Count);
                if (Count <= 1) // Could have blocking Dequeue thread(s).
                    Monitor.PulseAll(_Lock);
            }
        }

        static int DeQueue()
        {
            int x = 0;
            x = TSBuffer[Front];
            Front++;
            Front %= 10;
            Count -= 1;
            n++;
            return x;
        }

        static void th01()
        {
            int i;

            for (i = 1; i < 51; i++)
            {
                EnQueue(i);
                Thread.Sleep(5);
            }
        }

        static void th011()
        {
            int i;

            for (i = 100; i < 151; i++)
            {
                EnQueue(i);
                Thread.Sleep(5);
            }
        }

        static void th02(object t)
        {

            int j;

            for (int i = 0; i < 60; i++)
            {
                lock (_Lock)
                {
                    while (Count < 1)
                    {
                        Monitor.Wait(_Lock);
                        Console.WriteLine("Wait! : Empty stack");
                    }
                    j = DeQueue();
                    Console.WriteLine("\tj={0}, thread:{1}", j, t);
                    Thread.Sleep(100);
                    if (Count >= 10) // Could have blocking Dequeue thread(s).
                        Monitor.PulseAll(_Lock);
                }
                if(n >=101)
                {
                    Thread.Sleep(100);
                    Console.WriteLine("Finish!!");
                    Environment.Exit(0);
                }
            }
        }
        static void Main(string[] args)
        {
            Thread t1 = new Thread(th01);
            Thread t11 = new Thread(th011);
            Thread t2 = new Thread(th02);
            Thread t21 = new Thread(th02);
            Thread t22 = new Thread(th02);

            t1.Start();
            t11.Start();
            t2.Start(1);
            t21.Start(2);
            t22.Start(3);
        }

    }
}
