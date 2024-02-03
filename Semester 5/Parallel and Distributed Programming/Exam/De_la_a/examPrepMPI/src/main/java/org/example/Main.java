package org.example;

import mpi.MPI;

public class Main {
    public static void main(String[] args) {
        MPI.Init(args);
        int me = MPI.COMM_WORLD.Rank();
        int size = MPI.COMM_WORLD.Size();

        if (me == 0) {
/*
            int[] v1 = {1, 2, 3, 4, 5};
            int[] v2 = {1, 2, 3, 4, 5};
            Y2023no4.initializeMPI(v1, v2, size);
*/

            int[][] matrix = {
                    {3, 7, 4, 8},
                    {1, 5, 9, 2},
                    {6, 0, 3, 7}
            };

            Y2020no6.initializeMPI(798, size);


        } else {
            Y2020no6.computePrimeNumbersMPI(me);
        }

        MPI.Finalize();    }
}