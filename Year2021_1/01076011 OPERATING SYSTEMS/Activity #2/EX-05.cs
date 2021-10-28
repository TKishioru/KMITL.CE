using System;
using System.Diagnostics;
using System.Threading;

namespace OS_Sync_05
{
	class Program
	{
		private static string x = "";
		private static int exitflag = 0;
		private static int updateFlag = 0;
		static void ThReadX(object i)
		{
			while (exitflag == 0) {
				if (x != "exit") {
					Console.WriteLine("***Thread {0} : x = {1}***",i,x);
				}
			}
			Console.WriteLine("---Thread {0} exit---", i);
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
					x = xx;
			}
		}
			static void Main(string[] args)
			{
				Thread A = new Thread(ThWriteX);
				Thread B = new Thread(ThReadX);
				Thread C = new Thread(ThReadX);
				Thread D = new Thread(ThReadX);

				A.Start();
				B.Start(1);
				C.Start(2);
				D.Start(3);
		}
		}
	}
