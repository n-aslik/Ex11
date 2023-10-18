using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DrelLibrary;

namespace Drelclass
{
    internal class Program
    {
        static void Main(string[] args)
        {
            bool turnstatus = true;
            int score = 0;
            int command = 0;
            var Master = new Perfarator();

            while(turnstatus)
            {
                Console.WriteLine("Команды Дреля"+
                    "1-Start"+
                    "2-Reverse"+
                    "3-Speed"+
                    "4-Stop");
                command =Convert.ToInt32(Console.ReadLine());
                switch(command)
                {
                    case 1:
                        Master.Start();
                        break;
                    case 2:
                        Master.Reverse();
                        break;
                    case 3:
                        if(score==100)
                        {
                            Console.WriteLine($"Максимальная скорость: {score} ");
                        }
                        else
                        {
                            score = score + 5;
                            Master.Speed();
                            Console.WriteLine($"{Master.Volume + score}") ;
                        }
                        break;
                    case 4:
                        Master.Stop();
                        break;
                    default: 
                        Console.WriteLine("Не распознанная команда!");
                        break;
                }
            }


        }
    }
}
