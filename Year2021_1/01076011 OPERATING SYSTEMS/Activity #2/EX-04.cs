using System;
using System.Diagnostics;
using System.Threading;

namespace OS_Sync_04
{
	class Program
	{
		private static string x = "";
		private static int exitflag = 0;

		static void ThReadX()
		{
			while (exitflag == 0)
				Console.WriteLine("X = {0}", x);
		}

		static void ThWriteX()
		{
			string xx;
			while (exitflag == 0)
			{
				Console.WriteLine("Input: ");
				xx = Console.ReadLine();
				if (xx == "exit")
					exitflag = 1;
				else
					x = xx;
			}
		}
			static void Main(string[] args)
			{
				Thread A = new Thread(ThReadX);
				Thread B = new Thread(ThWriteX);

				A.Start();
				B.Start();
			}
		}
	}
