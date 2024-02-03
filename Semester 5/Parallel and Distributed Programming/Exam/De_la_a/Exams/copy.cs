using System.Text;

namespace Exams
{
    public class bignumsa
    {
        public void Main(string[] args)
        {
            //string a = "673486734348798273465678";
            //string b = "1273287389748974987698570975676";
            string a = "9999";
            string b = "999";

            int numberOfTasks = 4;

            if (a == "0" || b == "0")
            {
                Console.WriteLine("0");
                return;
            }


            string product = ParallelStringMultiply(a, b, numberOfTasks);
            Console.WriteLine("The Product is: " + product);
        }

        static void computePartialResult(string a, string b, int m, int n, int start, int end, int[] product, object[] locks)
        {
            int carry = 0;

            for (int i = start; i < end; i++)
            {
                int ai = a[m - 1 - i] - '0';

                for (int j = 0; j < n; j++)
                {
                    int bj = b[n - 1 - j] - '0';

                    lock (locks[i + j])
                    {
                        product[i + j] += ai * bj + carry;
                        carry = product[i + j] / 10;
                        product[i + j] %= 10;
                    }
                }
            }

            if (carry != 0)
            {
                lock (locks[m + n - 1])
                {
                    product[m + n - 1] = carry;
                }
            }


        }


        static string ParallelStringMultiply(string a, string b, int numberOfTasks)
        {
            if (b.Length > a.Length)
            {
                string aux = a;
                a = b;
                b = aux;
            }

            int m = a.Length;
            int n = b.Length;

            int[] product = new int[m + n];
            int chunkSize = m / numberOfTasks;
            var locks = new object[m + n];
            for (int i = 0; i < m + n; i++)
            {
                locks[i] = new object();
            }


            Task[] tasks = new Task[numberOfTasks];

            for (int taskIndex = 0; taskIndex < numberOfTasks; taskIndex++)
            {
                int start = taskIndex * chunkSize;
                int end = (taskIndex + 1) * chunkSize;
                if (taskIndex == numberOfTasks - 1)
                {
                    end = m;
                }

                tasks[taskIndex] = Task.Run(() => computePartialResult(a, b, m, n, start, end, product, locks));
            }

            Task.WaitAll(tasks);

            int carry = 0;
            //for (int i = 0; i < product.Length; i++)
            //{
            //    int total = product[i] + carry;
            //    product[i] = total % 10;
            //    carry = total / 10;
            //}

            StringBuilder sb = new StringBuilder();
            bool leadingZero = true;
            for (int i = product.Length - 1; i >= 0; i--)
            {
                if (product[i] != 0 || !leadingZero)
                {
                    sb.Append(product[i]);
                    leadingZero = false;
                }
            }

            return sb.ToString();
        }
    }
}