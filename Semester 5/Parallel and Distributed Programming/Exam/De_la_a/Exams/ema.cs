namespace Exams
{
    public class ema
    {
        public void Main(string[] args)
        {
            //var noThreads = int.Parse(args[0]);
            var noThreads = 4;

            var a = new int[3, 3]
            {
                { 1, 2, 3 },
                { 3, 2, 1 },
                { 4, 5, 6 }
            };

            var b = new int[3, 3]
            {
                { 1, 2, 3 },
                { 5, 6, 7 },
                { 8, 9, 1 }
            };

            var result = Multiply(a, b, noThreads);

            for (int i = 0; i < result.GetLength(0); i++)
            {
                for (int j = 0; j < result.GetLength(1); j++)
                {
                    Console.Write($"{result[i, j]} ");
                }

                Console.WriteLine();
            }
        }

        private int[,] Multiply(int[,] a, int[,] b, int noThreads)
        {
            var result = new int[a.GetLength(0), b.GetLength(1)];

            var chunkSize = a.GetLength(0) / noThreads;

            var tasks = new Task[noThreads];
            
            for (int i = 0; i < noThreads; i++)
            {
                var startLine = i * chunkSize;
                var stopLine = (i + 1) * chunkSize;

                if (i == noThreads - 1)
                {
                    stopLine = a.GetLength(0);
                }

                tasks[i] = Task.Run(() => MultiplyChunk(a, b, result, startLine, stopLine));
            }

            Task.WaitAll(tasks);

            return result;
        }


        private void MultiplyChunk(int[,] a, int[,] b, int[,] result, int startLine, int stopLine)
        {
            for (int i = startLine; i < stopLine; i++)
            {
                for (int j = 0; j < result.GetLength(1); j++)
                {
                    for (int k = 0; k < a.GetLength(1); k++)
                    {
                        result[i, j] += a[i, k] * b[k, j];
                    }
                }
            }
        }
    }
}