package org.example;

import mpi.MPI;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Y2020no6 {

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
    private static boolean isPrime(int number, int[] primes) {
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

    private static int[] combineResultsFromProcesses(int[][] results) {
        List<Integer> resultList = new ArrayList<>();

        for (int[] r : results) {
            for (int value : r) {
                resultList.add(value);
            }
        }

        return resultList.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }

    public static void initializeMPI(int n, int size) {

        int sqrtN = (int) Math.sqrt(n);

        List<Integer> primes = generatePrimes(sqrtN);
        int[] primesArray = primes.stream()
                .mapToInt(Integer::intValue)
                .toArray();

        int chunkSize = (n - sqrtN - 1) / (size - 1);
        for (int process = 1; process < size; process++) {

            int start = sqrtN + 1 + chunkSize * (process - 1);
            int end;
            if(process == size - 1){
                end = n;
            } else {
                end = start + chunkSize ;
            }

            MPI.COMM_WORLD.Send(new int[]{start}, 0, 1, MPI.INT, process, 0);
            MPI.COMM_WORLD.Send(new int[]{end}, 0, 1, MPI.INT, process, 0);

            MPI.COMM_WORLD.Send(new int[]{primesArray.length}, 0, 1, MPI.INT, process, 0);
            MPI.COMM_WORLD.Send(primesArray, 0, primesArray.length, MPI.INT, process, 0);
        }

        int[][] results = new int[size - 1][];
        int[] length = new int[size - 1];

        for (int process = 1; process < size; process++) {
            MPI.COMM_WORLD.Recv(length, process - 1 , 1, MPI.INT, process, 0);

            results[process - 1] = new int[length[process - 1]];
            MPI.COMM_WORLD.Recv(results[process - 1], 0 , length[process - 1], MPI.INT, process, 0);
        }

        int[] finalResult = combineResultsFromProcesses(results);

        System.out.println(Arrays.toString(finalResult));
    }

    public static void computePrimeNumbersMPI(int me)  {

        int[] start = new int[1];
        MPI.COMM_WORLD.Recv(start, 0, 1, MPI.INT, 0, 0);

        int[] end = new int[1];
        MPI.COMM_WORLD.Recv(end, 0, 1, MPI.INT, 0, 0);

        int[] length = new int[1];
        MPI.COMM_WORLD.Recv(length, 0, 1, MPI.INT, 0, 0);

        int[] primes = new int[length[0]];
        MPI.COMM_WORLD.Recv(primes, 0, length[0], MPI.INT, 0, 0);

        int[] result = IntStream.rangeClosed(start[0], end[0])
                .filter(i -> isPrime(i, primes))
                .toArray();

        MPI.COMM_WORLD.Send(new int[]{result.length}, 0, 1, MPI.INT, 0, 0);
        MPI.COMM_WORLD.Send(result, 0, result.length, MPI.INT, 0, 0);
    }
}
