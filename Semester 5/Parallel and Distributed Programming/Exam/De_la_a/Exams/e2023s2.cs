namespace Exams
{
    public class e2023s2
    {
        public int Main()
        {
            var matrix = new int[3, 3]
            {
                { 1, 1, 1 },
                { 1, 1, 1 },
                { 1, 1, 1 }
            };

            var sum = ComputeSum(matrix,  0, 3, 3);

            Console.WriteLine(sum);

            return 0;
        }

        private int ComputeSum(int[,] matrix, int startLine, int stopLine, int noThreads)
        {
            if (startLine == stopLine - 1)
            {
                var sum = 0;

                for (int i = 0; i < matrix.GetLength(1); i++)
                {
                    sum += matrix[startLine, i];
                }

                return sum;
            }

            var middleLine = (startLine + stopLine) / 2;

            if (noThreads <= 1)
            {
                var leftSumI = ComputeSum(matrix, startLine, middleLine, noThreads);
                var rightSumI = ComputeSum(matrix, middleLine, stopLine, noThreads);

                return leftSumI + rightSumI;
            }


            var leftSumTask = Task.Run(() => ComputeSum(matrix, startLine, middleLine, noThreads / 2));

            var rightSum = ComputeSum(matrix, middleLine, stopLine, noThreads - noThreads / 2);

            var leftSum = leftSumTask.Result;
            return leftSum + rightSum;
        }
    }
}