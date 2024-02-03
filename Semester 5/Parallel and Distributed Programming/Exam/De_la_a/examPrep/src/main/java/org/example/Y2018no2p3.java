package org.example;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class Y2018no2p3 {

    public static boolean canMultiply(int[][] matrixA, int[][] matrixB) {
        int columnsA = matrixA[0].length; // Number of columns in A
        int rowsB = matrixB.length;       // Number of rows in B

        return columnsA == rowsB;
    }

    private static int[][] addMatrices(int[][] matrixA, int[][] matrixB) {
        int numRows = matrixA.length;
        int numCols = matrixA[0].length;

        if (numRows != matrixB.length || numCols != matrixB[0].length) {
            throw new IllegalArgumentException("Matrices must have the same dimensions for addition.");
        }

        int[][] result = new int[numRows][numCols];

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < numCols; j++) {
                result[i][j] = matrixA[i][j] + matrixB[i][j];
            }
        }

        return result;
    }

    private static int[][] computeProdMatrixParallel(int[][] m1, int[][] m2, int start, int end, int noThreads, ExecutorService executor) throws ExecutionException, InterruptedException {

        if (start == end - 1) {
            return computeProdMatrix(m1, m2, start, end);
        }

        int middle = (start + end) / 2;
        if (noThreads <= 1) {
            int[][] left = computeProdMatrix(m1, m2, start, end);
            int[][] right = computeProdMatrix(m1, m2, start, end);
            return addMatrices(left, right);
        }

        Future<int[][]> leftFuture = executor.submit(() -> computeProdMatrixParallel(m1, m2, start, middle, noThreads / 2, executor));
        int[][] right = computeProdMatrixParallel(m1, m2, middle, end, noThreads / 2, executor);

        int[][] left = leftFuture.get();

        return addMatrices(left, right);
    }

    private static int computeElement(int[] row, int[] col) {
        int result = 0;

        for (int i = 0; i < row.length; i++) {
            result += row[i] * col[i];
        }

        return result;
    }

    private static int[][] computeProdMatrix(int[][] m1, int[][] m2, int start, int end) {
        int numRowsM1 = m1.length;    // Number of rows in the first matrix
        int numColsM2 = m2[0].length; // Number of columns in the second matrix
        int[][] result = new int[numRowsM1][numColsM2];

        for (int i = start; i < end; i++) {
            for (int j = 0; j < numColsM2; j++) {
                int[] row = m1[i]; // Get the current row from the first matrix
                int[] col = getNthColumn(m2, j);

                // Compute the scalar product of the row from the first matrix and the column from the second matrix
                result[i][j] = computeElement(row, col);
            }
        }

        // You can return the 'result' matrix or process it further as needed
        return result;
    }

    public static int[] getNthColumn(int[][] matrix, int n) {
        if (matrix == null || matrix.length == 0 || n < 0 || n >= matrix[0].length) {
            // Handle invalid input or out-of-bounds column index
            return new int[0]; // Return an empty array or handle the error as needed
        }

        int numRows = matrix.length;
        int[] column = new int[numRows];

        for (int i = 0; i < numRows; i++) {
            column[i] = matrix[i][n];
        }

        return column;
    }

    public static void callThreads() throws ExecutionException, InterruptedException {
        int[][] m1 = {
                {3, 7, 4, 8},
                {1, 5, 9, 2},
                {6, 0, 3, 7}
        };
        int[][] m2 = {
                {3, 7, 4, 8},
                {1, 5, 9, 2},
                {6, 0, 3, 7},
                {6, 0, 3, 7},
        };
        if (canMultiply(m1, m2)) {
            int startIndex = 0;
            int endIndex = m1.length;
            int noThreads = 1; // You can adjust this number to test with different thread counts
            try {
                ExecutorService executor = Executors.newFixedThreadPool(noThreads);
                int[][] result = computeProdMatrixParallel(m1, m2, startIndex, endIndex, noThreads, executor);
                executor.shutdown(); // always remember to shut down the executor
                for (int[] row : result) {
                    for (int value : row) {
                        System.out.print(value + " ");
                    }
                    System.out.println(); // Move to the next row
                }

            } catch (InterruptedException | ExecutionException e) {
                e.printStackTrace();
            }
        }
    }



    public static int[][] matrixMultiply(int[][] A, int[][] B, int numThreads) {
        if (A[0].length != B.length) {
            throw new IllegalArgumentException("Number of columns in A must equal number of rows in B");
        }

        int m = A.length;
        int n = B.length;
        int p = B[0].length;
        int[][] result = new int[m][p];

        ExecutorService executor = Executors.newFixedThreadPool(numThreads);
        List<Future<?>> futures = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < p; j++) {
                int finalI = i;
                int finalJ = j;
                futures.add(executor.submit(() -> {
                    for (int k = 0; k < n; k++) {
                        synchronized (result) {
                            result[finalI][finalJ] += A[finalI][k] * B[k][finalJ];
                        }
                    }
                }));
            }
        }

        // Wait for all tasks to complete
        for (Future<?> future : futures) {
            try {
                future.get();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }

        executor.shutdown();
        return result;
    }

    public static void main(String[] args) {
        int[][] matrixA = {
                {1, 2, 3},
                {4, 5, 6}
        };
        int[][] matrixB = {
                {7, 8},
                {9, 10},
                {11, 12}
        };
        int numThreads = 4; // Specify the number of threads

        int[][] result = matrixMultiply(matrixA, matrixB, numThreads);

        // Print the result
        for (int[] row : result) {
            for (int value : row) {
                System.out.print(value + " ");
            }
            System.out.println();
        }
    }
}
