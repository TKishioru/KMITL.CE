# Operating System 
<details>
<summary><b>Table of Contents</b> (click to open)</summary>
<!-- MarkdownTOC -->

⌦ [Introduction](#Introduction)
    
⌦ [Kernel](#Kernel)
    
⌦ [Structure](#Structure)
    
⌦ [Concurrency](#Concurrency)
    
⌦ [Synchronization + Advance Synchronization](#synchronization--advance-synchronization)
    
⌦ [Scheduling](#Scheduling)
    
⌦ [Address Translation](#address-translation)
    
⌦ [Caching + Virtual Memory](#caching--virtual-memory)

<!-- /MarkdownTOC -->
</details>

## Introduction

```
What’s an Operating System?
```

เป็น software ที่ใช้ในการจัดการ resource ต่างๆภายในคอมพิวเตอร์ ซึ่ง resource เป็นพวก Hardware ต่างๆ เช่น CPU , mouse , keyboard , RAM

```
Roles of the Operating System
```

1. Referee
    - กรรมการที่คอยตัดสินใจว่าใครจะได้ใช้ resource ใด? เมื่อไร?
    - ต้องมีความ Isolation
    - Communication
2. illusionist
    - สร้าง illusion ขึ้นมาว่า program ที่กำลัง run อยู่สามารถใช้งานได้เต็มกำลัง ใช้ได้ทั้งเครื่อง
3. Glue เชื่อม library เข้าด้วยกัน (ระหว่าง interface, Libraries)

```
Operating System Evaluation
```

1.	Reliability : ต้องมีความเสถียร
2.	Availability : ต้องพร้อมใช้งานตลอดเวลา
3.	Security : ป้องกันพวกไวรัส
4.	Privacy : แบ่งแยกไฟล์ของแต่ละ ex.ไฟล์ของ application ใดก็มีแต่ app นั้นๆที่สามารถเข้าถึงได้
5.	Portability : สามารถเคลื่อนย้ายโปรแกรมได้
    - For programs
    
       ต้องพิจารณา API,Abstraction virtual machine
    - For OS    ``` “hardware abstraction layer” ```
    
       เป็นการสร้าง Abstraction ที่ใช้ในการอ้างอิงระหว่างฝั่ง hardware กับฝั่งที่เป็นคนเขียน operating system
6.	Performance
    - Latency : ความเร็วในส่วนของ response
    - Throughput : จำนวนงานที่ทำได้ per time unit
    - Overhead : ให้ overhead น้อย
    - Fairness : ความ fair ของการใช้งานของแต่ละ program
    - Predictability

> Early operating system
- รัน 1 application ต่อ 1 หน่วยเวลา
- Batch system
- Computer แพง

> Time-sharing operating system
- เริ่มให้หลาย user ทำงานพร้อมกันในช่วงเวลานึงได้ (multiprocessing)
- ราคาเริ่มถูกลง

> TODAY’s computer is cheap

> Tomorrow
- data center ใหญ่ขึ้นต้องรองรับให้ได้

## Kernel

## Structure

## Concurrency

<details>
<summary>Experiment #1</summary>

```C#
// simple thread - test order
using System;
using System.Threading;

namespace Lab_OS_Concurrency
{
    class Program
    {
        static void TestThread1()
        {
            for(int i = 0; i < 100; i++)
                Console.WriteLine("Thread# 1 i = {0}",i);
        }
        static void TestThread2()
        {
            for(int i = 0; i < 100; i++)
                Console.WriteLine("Thread# 2 i = {0}",i);
        }
        static void Main(string[] args)
        {
            Thread th1 = new Thread(TestThread1);
            Thread th2 = new Thread(TestThread2);
            th1.Start();
            th2.Start();
        }
    }
}
```
</details>


<details>
<summary>Experiment #2</summary>

```C#
// test resource sharing
using System;
using System.Threading;

namespace Lab_OS_Concurrency01
{
    class Program
    {
        static int resource = 10000;
        static void TestThread1()
        {
            Console.WriteLine("Thread# 1 i = {0}",resource);
        }
        static void TestThread2()
        {
            Console.WriteLine("Thread# 2 i = {0}",resource);
        }
        static void Main(string[] args)
        {
            Thread th1 = new Thread(TestThread1);
            Thread th2 = new Thread(TestThread2);
            th1.Start();
            th2.Start();
        }
    }
}
```
</details>


<details>
<summary>Experiment #3</summary>

```C#
// test pause a thread
using System;
using System.Threading;

namespace Lab_OS_Concurrency02
{
    class Program
    {
        static int resource = 10000;
        static void TestThread1()
        {
            resource = 55555;
        }
        static void Main(string[] args)
        {
            Thread th1 = new Thread(TestThread1);
            th1.Start();
            //Thread.Sleep(10);
            Console.WriteLine("resource = {0}",resource);
        }
    }
}
```
    

```C#
// test pause 2
using System;
using System.Threading;

namespace Lab_OS_Concurrency01
{
    class Program
    {
        static int resource = 10000;
        static void TestThread1()
        {
            for(int i = 0; i < 45555; i++)
            {
                resource++;
                Console.Write(".");
            }
        }
        static void Main(string[] args)
        {
            Thread th1 = new Thread(TestThread1);
            th1.Start();
            Thread.Sleep(10);
            Console.WriteLine("resource = {0}",resource);
        }
    }
}
```
    
</details>


<details>
<summary>Experiment #4</summary>

```C#
// test pause 2
using System;
using System.Threading;

namespace Lab_OS_Concurrency01
{
    class Program
    {
        static int resource = 10000;
        static void TestThread1()
        {
            for(int i = 0; i < 45555; i++)
            {
                resource++;
                Console.Write(".");
            }
        }
        static void Main(string[] args)
        {
            Thread th1 = new Thread(TestThread1);
            th1.Start();
            //Thread.Sleep(10);
            th1.Join();
            Console.WriteLine("resource = {0}",resource);
        }
    }
}
```
</details>
    
## Synchronization + Advance Synchronization

## Scheduling

## Address Translation

## Caching + Virtual Memory
