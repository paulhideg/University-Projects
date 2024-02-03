package org.example;

import java.util.Arrays;
import java.util.concurrent.*;

public class Y2018no2p1 {

    public static void main(String[] args) throws InterruptedException {
        int n = 3;
        int[] a = new int[n];
        int[] b = new int[n];
        int[] res = new int[n];
        //int[] res = new int[2 * n];

        a[0] = 1;
        a[1] = 2;
        a[2] = 3;

        b[0] = 1;
        b[1] = 2;
        b[2] = 3;

        int threads = 2;
        int chunkSize = (n * 2 - 1) / threads;

        ExecutorService executor = Executors.newFixedThreadPool(threads);

        for (int i = 0; i < threads; i++) {
            int start = chunkSize * i;
            int stop;

            if (i == threads - 1) {
                stop = 2 * n - 1;
            } else {
                stop = chunkSize * (i + 1);
            }

            executor.execute(() -> conv(start, stop, a, b, n, res));
        }

        executor.shutdown();
        executor.awaitTermination(Long.MAX_VALUE, TimeUnit.NANOSECONDS);

        System.out.println(Arrays.toString(Arrays.stream(res).toArray()));
    }

    public static void conv(int start, int stop, int[] a, int[] b, int n, int[] res) {
        for (int i = start; i < stop; i++) {
            for (int j = 0; j < n; j++) {
                if (i - j >= 0) {
                    res[i % n] += a[j] * b[(i - j) % n];
                }
                /*if (i - j >= 0 && i - j < n)
                {
                    res[i] += a[j] * b[i - j];
                }*/
            }
        }
    }
}
