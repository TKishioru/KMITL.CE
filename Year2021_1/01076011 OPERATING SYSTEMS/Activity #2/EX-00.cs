using System;
using System.Diagnostics;
using System.Threading;

namespace OS_Sync_Ex_00
{
	class Program
	{
		private static int sum = 0;

		static void plus()
		{
			int i;
			for (i = 1; i < 1000001; i++)
				sum += i;
		}

		static void minus()
		{
			int i;
			for (i = 1; i < 1000000; i++)
				sum -= i;
		}

		static void Main(string[] args)
		{
			Stopwatch sw = new Stopwatch();
			Console.WriteLine("Start...");
			sw.Start();
			plus();
			minus();
			sw.Stop();
			Console.WriteLine("sum ={0}", sum);
			Console.WriteLine("Time used: " + sw.ElapsedMilliseconds.ToString() + "ms");
		}
	}
}
