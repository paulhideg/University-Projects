package org.example;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class Y2018no3 {

    public static BigInteger karatsuba(BigInteger x, BigInteger y, int numThreads) {
        int n = Math.max(x.bitLength(), y.bitLength());
        if (n <= 2000 || numThreads <= 1) {
            // For small inputs or single thread, use regular multiplication
            return x.multiply(y);
        }

        // Split the input numbers into two parts
        int half = (n + 32) / 64 * 32;
        BigInteger mask = BigInteger.ONE.shiftLeft(half).subtract(BigInteger.ONE);
        BigInteger xLow = x.and(mask);
        BigInteger xHigh = x.shiftRight(half);
        BigInteger yLow = y.and(mask);
        BigInteger yHigh = y.shiftRight(half);

        // Create a thread pool with the specified number of threads
        ExecutorService executor = Executors.newFixedThreadPool(numThreads);
        List<Future<BigInteger>> results = new ArrayList<>();

        // Submit recursive tasks for each split part
        results.add(executor.submit(() -> karatsuba(xHigh, yHigh, numThreads / 2)));
        results.add(executor.submit(() -> karatsuba(xLow.add(xHigh), yLow.add(yHigh), numThreads / 2)));
        results.add(executor.submit(() -> karatsuba(xLow, yLow, numThreads / 2)));

        // Combine the results
        try {
            BigInteger a = results.get(0).get();
            BigInteger b = results.get(1).get();
            BigInteger c = results.get(2).get();

            BigInteger firstTerm = a.shiftLeft(2 * half);
            BigInteger secondTerm = (b.subtract(a).subtract(c)).shiftLeft(half);
            BigInteger result = firstTerm.add(secondTerm).add(c);
            return result;
        } catch (Exception e) {
            e.printStackTrace();
            return BigInteger.ZERO;
        } finally {
            executor.shutdown();
        }
    }

    public static void main(String[] args) {
        BigInteger num1 = new BigInteger("1267890");
        BigInteger num2 = new BigInteger("98765410");
        int numThreads = 4; // Specify the number of threads

        BigInteger product = karatsuba(num1, num2, numThreads);

        System.out.println("Product: " + product);
    }
}
