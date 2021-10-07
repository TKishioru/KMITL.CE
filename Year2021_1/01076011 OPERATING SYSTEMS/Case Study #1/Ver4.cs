//MultiThread 8 Core

using System;
using System.Diagnostics;
using System.IO;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.Threading;

namespace Problem01
{
    class Program
    {
        static byte[] Data_Global = new byte[1000000000];
        static long Sum_Global1 = 0, Sum_Global2 = 0, Sum_Global3 = 0, Sum_Global4 = 0, Sum_Global5 = 0, Sum_Global6 = 0, Sum_Global7 = 0, Sum_Global8 = 0;

        static int ReadData()
        {
            int returnData = 0;
            FileStream fs = new FileStream("Problem01.dat", FileMode.Open);
            BinaryFormatter bf = new BinaryFormatter();

            try
            {
                Data_Global = (byte[])bf.Deserialize(fs);
            }
            catch (SerializationException se)
            {
                Console.WriteLine("Read Failed:" + se.Message);
                returnData = 1;
            }
            finally
            {
                fs.Close();
            }

            return returnData;
        }
        static void sum1()
        {
            int G_index = 0;
            for (int i = 0; i < 125000000; i++)
            {
                if (Data_Global[G_index] % 2 == 0)
                {
                    Sum_Global1 -= Data_Global[G_index];
                }
                else if (Data_Global[G_index] % 3 == 0)
                {
                    Sum_Global1 += (Data_Global[G_index] * 2);
                }
                else if (Data_Global[G_index] % 5 == 0)
                {
                    Sum_Global1 += (Data_Global[G_index] / 2);
                }
                else if (Data_Global[G_index] % 7 == 0)
                {
                    Sum_Global1 += (Data_Global[G_index] / 3);
                }
                Data_Global[G_index] = 0;
                G_index += 8;
            }
        }

        static void sum2()
        {
            int G_index = 1;
            for (int i = 0; i < 125000000; i++)
            {
                if (Data_Global[G_index] % 2 == 0)
                {
                    Sum_Global2 -= Data_Global[G_index];
                }
                else if (Data_Global[G_index] % 3 == 0)
                {
                    Sum_Global2 += (Data_Global[G_index] * 2);
                }
                else if (Data_Global[G_index] % 5 == 0)
                {
                    Sum_Global2 += (Data_Global[G_index] / 2);
                }
                else if (Data_Global[G_index] % 7 == 0)
                {
                    Sum_Global2 += (Data_Global[G_index] / 3);
                }
                Data_Global[G_index] = 0;
                G_index += 8;
            }
        }
        static void sum3()
        {
            int G_index = 2;
            for (int i = 0; i < 125000000; i++)
            {
                if (Data_Global[G_index] % 2 == 0)
                {
                    Sum_Global3 -= Data_Global[G_index];
                }
                else if (Data_Global[G_index] % 3 == 0)
                {
                    Sum_Global3 += (Data_Global[G_index] * 2);
                }
                else if (Data_Global[G_index] % 5 == 0)
                {
                    Sum_Global3 += (Data_Global[G_index] / 2);
                }
                else if (Data_Global[G_index] % 7 == 0)
                {
                    Sum_Global3 += (Data_Global[G_index] / 3);
                }
                Data_Global[G_index] = 0;
                G_index += 8;
            }
        }
        static void sum4()
        {
            int G_index = 3;
            for (int i = 0; i < 125000000; i++)
            {
                if (Data_Global[G_index] % 2 == 0)
                {
                    Sum_Global4 -= Data_Global[G_index];
                }
                else if (Data_Global[G_index] % 3 == 0)
                {
                    Sum_Global4 += (Data_Global[G_index] * 2);
                }
                else if (Data_Global[G_index] % 5 == 0)
                {
                    Sum_Global4 += (Data_Global[G_index] / 2);
                }
                else if (Data_Global[G_index] % 7 == 0)
                {
                    Sum_Global4 += (Data_Global[G_index] / 3);
                }
                Data_Global[G_index] = 0;
                G_index += 8;
            }
        }
        static void sum5()
        {
            int G_index = 4;
            for (int i = 0; i < 125000000; i++)
            {
                if (Data_Global[G_index] % 2 == 0)
                {
                    Sum_Global5 -= Data_Global[G_index];
                }
                else if (Data_Global[G_index] % 3 == 0)
                {
                    Sum_Global5 += (Data_Global[G_index] * 2);
                }
                else if (Data_Global[G_index] % 5 == 0)
                {
                    Sum_Global5 += (Data_Global[G_index] / 2);
                }
                else if (Data_Global[G_index] % 7 == 0)
                {
                    Sum_Global5 += (Data_Global[G_index] / 3);
                }
                Data_Global[G_index] = 0;
                G_index += 8;
            }
        }
        static void sum6()
        {
            int G_index = 5;
            for (int i = 0; i < 125000000; i++)
            {
                if (Data_Global[G_index] % 2 == 0)
                {
                    Sum_Global6 -= Data_Global[G_index];
                }
                else if (Data_Global[G_index] % 3 == 0)
                {
                    Sum_Global6 += (Data_Global[G_index] * 2);
                }
                else if (Data_Global[G_index] % 5 == 0)
                {
                    Sum_Global6 += (Data_Global[G_index] / 2);
                }
                else if (Data_Global[G_index] % 7 == 0)
                {
                    Sum_Global6 += (Data_Global[G_index] / 3);
                }
                Data_Global[G_index] = 0;
                G_index += 8;
            }
        }

        static void sum7()
        {
            int G_index = 6;
            for (int i = 0; i < 125000000; i++)
            {
                if (Data_Global[G_index] % 2 == 0)
                {
                    Sum_Global7 -= Data_Global[G_index];
                }
                else if (Data_Global[G_index] % 3 == 0)
                {
                    Sum_Global7 += (Data_Global[G_index] * 2);
                }
                else if (Data_Global[G_index] % 5 == 0)
                {
                    Sum_Global7 += (Data_Global[G_index] / 2);
                }
                else if (Data_Global[G_index] % 7 == 0)
                {
                    Sum_Global7 += (Data_Global[G_index] / 3);
                }
                Data_Global[G_index] = 0;
                G_index += 8;
            }
        }

        static void sum8()
        {
            int G_index = 7;
            for (int i = 0; i < 125000000; i++)
            {
                if (Data_Global[G_index] % 2 == 0)
                {
                    Sum_Global8 -= Data_Global[G_index];
                }
                else if (Data_Global[G_index] % 3 == 0)
                {
                    Sum_Global8 += (Data_Global[G_index] * 2);
                }
                else if (Data_Global[G_index] % 5 == 0)
                {
                    Sum_Global8 += (Data_Global[G_index] / 2);
                }
                else if (Data_Global[G_index] % 7 == 0)
                {
                    Sum_Global8 += (Data_Global[G_index] / 3);
                }
                Data_Global[G_index] = 0;
                G_index += 8;
            }
        }
        static void Main(string[] args)
        {
            Stopwatch sw = new Stopwatch();
            Thread th1 = new Thread(sum1);
            Thread th2 = new Thread(sum2);
            Thread th3 = new Thread(sum3);
            Thread th4 = new Thread(sum4);
            Thread th5 = new Thread(sum5);
            Thread th6 = new Thread(sum6);
            Thread th7 = new Thread(sum7);
            Thread th8 = new Thread(sum8);
            /* Read data from file */
            Console.Write("Data read...");
            int y = ReadData();
            if (y == 0)
            {
                Console.WriteLine("Complete.");
            }
            else
            {
                Console.WriteLine("Read Failed!");
            }

            /* Start */
            Console.Write("\n\nWorking...");
            sw.Start();
            th1.Start();
            th2.Start();
            th3.Start();
            th4.Start();
            th5.Start();
            th6.Start();
            th7.Start();
            th8.Start();
            th1.Join();
            th2.Join();
            th3.Join();
            th4.Join();
            th5.Join();
            th6.Join();
            th7.Join();
            th8.Join();
            sw.Stop();
            Console.WriteLine("Done.");

            /* Result */
            Console.WriteLine("Summation result: {0}", Sum_Global1 + Sum_Global2 + Sum_Global3 + Sum_Global4 + Sum_Global5 + Sum_Global6 + Sum_Global7 + Sum_Global8);
            Console.WriteLine("Time used: " + sw.ElapsedMilliseconds.ToString() + "ms");
        }
    }
}
