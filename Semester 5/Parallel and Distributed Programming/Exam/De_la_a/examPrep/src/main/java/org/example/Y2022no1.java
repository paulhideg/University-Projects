package org.example;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Y2022no1 {

    private static List<Integer> generatePrimes(int max) {
        boolean[] isPrime = new boolean[max + 1];
        List<Integer> primes = new ArrayList<>();

        for (int i = 2; i <= max; i++) {
            isPrime[i] = true;
        }

        for (int p = 2; p * p <= max; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i <= max; i += p) {
                    isPrime[i] = false;
                }
            }
        }

        for (int i = 2; i <= max; i++) {
            if (isPrime[i]) {
                primes.add(i);
            }
        }

        return primes;
    }

    // Function to check if a number is prime using the list of primes
    private static boolean isPrime(int number, List<Integer> primes) {
        if (number < 2) {
            return false;
        }

        for (int prime : primes) {
            if (prime * prime > number) {
                break;
            }
            if (number % prime == 0) {
                return false;
            }
        }

        return true;
    }

    public static  List<Integer> computePrimeNumbersParallel(int start, int end, List<Integer> primes, int noThreads, ExecutorService executor) throws ExecutionException, InterruptedException {
        if (noThreads <= 1 || end - start <= 1) {
            return IntStream.rangeClosed(start, end)
                    .filter(i -> isPrime(i, primes))
                    .boxed()
                    .collect(Collectors.toList());
        }

        int middle = (start + end) / 2;

        Future<List<Integer>> leftFuture = executor.submit(() -> computePrimeNumbersParallel(start, middle, primes, noThreads / 2, executor));
        List<Integer> right = computePrimeNumbersParallel(middle, end, primes, noThreads / 2, executor);

        List<Integer> left = leftFuture.get(); // waits for the thread to complete and retrieves the result
        left.addAll(right);

        return left;
    }

    public static void callThreads(){
        int n = 1287;
        int noThreads = 7; // You can adjust this number to test with different thread counts

        try {
            ExecutorService executor = Executors.newFixedThreadPool(noThreads);
            List<Integer> result = computePrimeNumbersParallel((int) Math.sqrt(n) + 1, n, generatePrimes((int) Math.sqrt(n)), noThreads, executor);
            executor.shutdown(); // always remember to shut down the executor
            System.out.println("Result: " + result.stream().toList());
        } catch (InterruptedException | ExecutionException e) {
            e.printStackTrace();
        }
    }

}
