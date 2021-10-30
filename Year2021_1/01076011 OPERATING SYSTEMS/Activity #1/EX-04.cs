using System;
using System.Diagnostics;
using System.Threading;

namespace OS_Sync_04
{
    class Program
    {
        private static string x = "";
        private static int exitflag = 0;
        private static int print = 1;
        private static int key = 0;
        private static Semaphore s;
        static void ThReadX()
        {

            while (exitflag == 0)
            {
                s.WaitOne();
                if (print == 0) Console.WriteLine("X = {0}", x);
                print = 1;
                key = 0;
                s.Release();
            }
        }

        static void ThWriteX()
        {
            //Console.WriteLine("ThWriteX");

            string xx;
            while (exitflag == 0)
            {
                if (key == 0)
                {
                    Console.Write("Input: ");
                    xx = Console.ReadLine();
                    if (xx == "exit")
                    {
                        s.WaitOne();
                        exitflag = 1;
                        Console.WriteLine("Thread 1 exit");
                        s.Release();
                    }
                    else if (xx != "")
                    {
                        s.WaitOne();
                        x = xx;
                        key = 1;
                        print = 0;
                        s.Release();
                    }
                }
            }
        }

        static void Main(string[] args)
        {
            Thread A = new Thread(ThReadX);
            Thread B = new Thread(ThWriteX);
            s = new Semaphore(1, 1);

            A.Start();
            B.Start();
        }
    }
}
