namespace Exams
{
    public class conv2
    {
        public void Main(string[] args)
        {
            int n = 3;
            int[] a = new int[n];
            int[] b = new int[n];
            int[] res = new int[2 * n];

            a[0] = 1;
            a[1] = 2;
            a[2] = 3;

            b[0] = 1;
            b[1] = 2;
            b[2] = 3;

            int threads = 2;
            int chunkSize = (n * 2 - 1) / threads;

            Task[] tasks = new Task[threads];

            for (int i = 0; i < threads; i++)
            {
                int start = chunkSize * i;
                int stop = chunkSize * (i + 1);

                if (i == threads - 1)
                {
                    stop = 2 * n - 1;
                }

                tasks[i] = Task.Run(() => Conv(start, stop, a, b, n, res));
            }

            Task.WaitAll(tasks);

            for (int i = 0; i < 2 * n - 1; i++)
            {
                Console.Write($"{res[i]} ");
            }

        }

        public void Conv(int start, int stop, int[] a, int[] b, int n, int[] res)
        {
            for (int i = start; i < stop; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    if (i - j >= 0 && i - j < n)
                    {
                        res[i] += a[j] * b[i - j];
                    }
                }
            }
        }
    }
}