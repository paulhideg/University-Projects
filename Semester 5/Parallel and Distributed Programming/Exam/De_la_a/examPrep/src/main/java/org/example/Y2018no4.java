package org.example;

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.ArrayList;
import java.util.List;

public class Y2018no4 {

    public static int[][] matrixMultiply(int[][] A, int[][] B) {
        int n = A.length;
        int[][] result = new int[n][n];
        ExecutorService executor = Executors.newFixedThreadPool(Runtime.getRuntime().availableProcessors());

        List<Future<?>> futures = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            int row = i;
            futures.add(executor.submit(() -> {
                for (int j = 0; j < n; j++) {
                    for (int k = 0; k < n; k++) {
                        result[row][j] += A[row][k] * B[k][j];
                    }
                }
            }));
        }

        // Wait for all threads to complete
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

    public static int[][] matrixPower(int[][] matrix, int exponent) {
        int n = matrix.length;

        if (exponent == 0) {
            int[][] identity = new int[n][n];
            for (int i = 0; i < n; i++) {
                identity[i][i] = 1;
            }
            return identity;
        }

        if (exponent == 1) {
            return matrix;
        }

        if (exponent % 2 == 0) {
            int[][] halfPower = matrixPower(matrix, exponent / 2);
            return matrixMultiply(halfPower, halfPower);
        } else {
            int[][] halfPower = matrixPower(matrix, (exponent - 1) / 2);
            int[][] temp = matrixMultiply(halfPower, halfPower);
            return matrixMultiply(matrix, temp);
        }
    }

    public static void main(String[] args) {
        int[][] matrix = {
                {1, 2},
                {3, 4}
        };
        int exponent = 3; // Change this to the desired exponent

        int[][] result = matrixPower(matrix, exponent);

        // Print the result
        for (int[] row : result) {
            for (int value : row) {
                System.out.print(value + " ");
            }
            System.out.println();
        }
    }
}
