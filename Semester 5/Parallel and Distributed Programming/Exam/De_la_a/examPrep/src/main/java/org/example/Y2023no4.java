package org.example;

import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class Y2023no4 {

    private static int computeProduct(int[] v1, int[] v2, int startIndex, int endIndex, int noThreads, ExecutorService executor) throws InterruptedException, ExecutionException {

        if (startIndex == endIndex - 1) {
            return v1[startIndex] * v2[startIndex];
        }

        int middle = (startIndex + endIndex) / 2;
        if (noThreads <= 1) {
            int left = computeProduct(v1, v2, startIndex, middle, noThreads, executor);
            int right = computeProduct(v1, v2, middle, endIndex, noThreads,executor);
            return left + right;
        }

        Future<Integer> leftFuture = executor.submit(() -> computeProduct(v1, v2, startIndex, middle, noThreads / 2, executor));
        int right = computeProduct(v1, v2, middle, endIndex, noThreads / 2, executor);

        int left = leftFuture.get(); // waits for the thread to complete and retrieves the result

        return left + right;
    }

    public static void callThreads(){
        int[] v1 = {1, 2, 3, 4, 5};
        int[] v2 = {1, 2, 3, 4, 5};
        int startIndex = 0;
        int endIndex = v1.length;
        int noThreads = 4; // You can adjust this number to test with different thread counts

        try {
            ExecutorService executor = Executors.newFixedThreadPool(noThreads);
            int result = computeProduct(v1, v2, startIndex, endIndex, noThreads, executor);
            executor.shutdown(); // always remember to shut down the executor
            System.out.println("Result: " + result);
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }
}
