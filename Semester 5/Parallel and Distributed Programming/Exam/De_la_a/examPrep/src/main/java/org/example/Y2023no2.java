package org.example;

import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class Y2023no2 {
    private static int computeSumMatrixParallel(int[][] matrix, int start, int end, int noThreads, ExecutorService executor) throws ExecutionException, InterruptedException {
        if(start == end - 1){
            return computeSumVector(matrix[start]);
        }

        int middle = (start + end) / 2;
        if(noThreads <= 1){
            int left = computeSumMatrix(matrix, start, middle);
            int right = computeSumMatrix(matrix, middle, end);
            return left  + right;
        }

        Future<Integer> leftFuture = executor.submit(() -> computeSumMatrixParallel(matrix, start, middle, noThreads / 2, executor));
        int right = computeSumMatrixParallel(matrix, middle, end, noThreads / 2, executor);

        int left = leftFuture.get();

        return right + left;
    }

    private static int computeSumMatrix(int[][] matrix, int start, int end) {
        int result = 0;
        for(int i=start; i<end; i++){
            result += computeSumVector(matrix[i]);
        }

        return result;
    }

    private static int computeSumVector(int[] vector){
        int result = 0;
        for (int j : vector) {
            result += j;
        }
        return result;
    }

    public static void callThreads(){
        int[][] matrix = {
                {3, 7, 4, 8},
                {1, 5, 9, 2},
                {6, 0, 3, 7}
        };
        int startIndex = 0;
        int endIndex = matrix.length;
        int noThreads = 1; // You can adjust this number to test with different thread counts

        try {
            ExecutorService executor = Executors.newFixedThreadPool(noThreads);
            int result = computeSumMatrixParallel(matrix, startIndex, endIndex, noThreads, executor);
            executor.shutdown(); // always remember to shut down the executor
            System.out.println("Result: " + result);
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }
}
