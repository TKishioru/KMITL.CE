//MultiThread 6 Core

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
        static long Sum_Global1 = 0, Sum_Global2 = 0, Sum_Global3 = 0, Sum_Global4 = 0, Sum_Global5 = 0, Sum_Global6 = 0, Sum_Global7 = 0, Sum_Global8 = 0,
                    Sum_Global9 = 0, Sum_Global10 = 0, Sum_Global11 = 0, Sum_Global12 = 0, Sum_Global13 = 0, Sum_Global14 = 0, Sum_Global15 = 0, Sum_Global16 = 0;

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
            for (int i = 0; i < 625000; i++)
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
                G_index += 16;
            }
        }

        static void sum2()
        {
            int G_index = 1;
            for (int i = 0; i < 625000; i++)
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
                G_index += 16;
            }
        }
        static void sum3()
        {
            int G_index = 2;
            for (int i = 0; i < 625000; i++)
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
                G_index += 16;
            }
        }
        static void sum4()
        {
            int G_index = 3;
            for (int i = 0; i < 625000; i++)
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
                G_index += 16;
            }
        }
        static void sum5()
        {
            int G_index = 4;
            for (int i = 0; i < 625000; i++)
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
                G_index += 16;
            }
        }
        static void sum6()
        {
            int G_index = 5;
            for (int i = 0; i < 625000; i++)
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
                G_index += 16;
            }
        }

        static void sum7()
        {
            int G_index = 6;
            for (int i = 0; i < 625000; i++)
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
                G_index += 16;
            }
        }

        static void sum8()
        {
            int G_index = 7;
            for (int i = 0; i < 625000; i++)
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
                G_index += 16;
            }
        }

        static void sum9()
        {
            int G_index = 8;
            for (int i = 0; i < 625000; i++)
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
                G_index += 16;
            }
        }

        static void sum10()
        {
            int G_index = 9;
            for (int i = 0; i < 625000; i++)
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
                G_index += 16;
            }
        }
        static void sum11()
        {
            int G_index = 10;
            for (int i = 0; i < 625000; i++)
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
                G_index += 16;
            }
        }
        static void sum12()
        {
            int G_index = 11;
            for (int i = 0; i < 625000; i++)
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
                G_index += 16;
            }
        }
        static void sum13()
        {
            int G_index = 12;
            for (int i = 0; i < 625000; i++)
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
                G_index += 16;
            }
        }
        static void sum14()
        {
            int G_index = 13;
            for (int i = 0; i < 625000; i++)
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
                G_index += 16;
            }
        }

        static void sum15()
        {
            int G_index = 14;
            for (int i = 0; i < 625000; i++)
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
                G_index += 16;
            }
        }

        static void sum16()
        {
            int G_index = 15;
            for (int i = 0; i < 625000; i++)
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
                G_index += 16;
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
            Thread th9 = new Thread(sum9);
            Thread th10 = new Thread(sum10);
            Thread th11 = new Thread(sum11);
            Thread th12 = new Thread(sum12);
            Thread th13 = new Thread(sum13);
            Thread th14 = new Thread(sum14);
            Thread th15 = new Thread(sum15);
            Thread th16 = new Thread(sum16);
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
            th9.Start();
            th10.Start();
            th11.Start();
            th12.Start();
            th13.Start();
            th14.Start();
            th15.Start();
            th16.Start();
            th1.Join();
            th2.Join();
            th3.Join();
            th4.Join();
            th5.Join();
            th6.Join();
            th7.Join();
            th8.Join();
            th9.Join();
            th10.Join();
            th11.Join();
            th12.Join();
            th13.Join();
            th14.Join();
            th15.Join();
            th16.Join();
            sw.Stop();
            Console.WriteLine("Done.");

            /* Result */
            //For 6 Core
            Console.WriteLine("Summation result: {0}", Sum_Global1 + Sum_Global2 + Sum_Global3 + Sum_Global4 + Sum_Global5 + Sum_Global6 + Sum_Global7 + Sum_Global8 + 
                Sum_Global9 + Sum_Global10 + Sum_Global11 + Sum_Global12 + Sum_Global13 + Sum_Global14 + Sum_Global15 + Sum_Global16);
            Console.WriteLine("Time used: " + sw.ElapsedMilliseconds.ToString() + "ms");
        }
    }
}
