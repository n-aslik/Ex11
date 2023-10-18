using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DrelLibrary
{
    public abstract class Drel
    {
        public abstract string Name { get; }
        public abstract bool Revers { get; }
        public abstract int Volume { get; }
        public bool Status { get; set; }



        public abstract void Start();
        public abstract void Stop();
        public abstract void Move();
        public abstract void Reverse();
        public abstract void Speed();





    }
    public class Perfarator : Drel
    {


        public override string Name => "TOTAL";

        public override int Volume => 0;

        public override bool Revers => false;



        public override void Start()
        {

            Task.Delay(100);
            if (!Status)
            {
                Status = true;
                System.Console.WriteLine($"Дрель {Name} включён");
                Move();
            }
        }
        public override void Stop()
        {
            if (Status)
            {
                Status = false;
                System.Console.WriteLine($"Дрель {Name} выключен");
            }
        }
        public override void Move()
        {
            Console.WriteLine("TRRRRRRRRRRRRRRRRRRRRRRRR");
        }


        public override void Reverse()
        {

            if (!Revers)
            {
                
                Console.WriteLine($"Дрель {Name} крутиться назад");
            }
            else
            {

                Move();
            }
        }

        public override void Speed()
        {

            if (Volume == 0)
            {

                System.Console.WriteLine($"Дрель {Name} поставлен на скорость:");


            }

            else
            {
                Stop();
            }
        }
    }
}
    

