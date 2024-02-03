package org.example;

import mpi.*;

public class Y2023no4 {

    public static int combineResultsFromProcesses(int[] polynomials) {

        int result = 0;
        for (int polynomial : polynomials) {
            result += polynomial;
        }

        return result;
    }

    public static void initializeMPI(int[] v1, int[] v2, int size) {

        int chunkSize = v1.length / (size - 1);
        for (int process = 1; process < size; process++) {

            int start = chunkSize * (process - 1);
            int end;
            if(process == size - 1){
                end = v1.length;
            } else {
                end = start + chunkSize ;
            }
            System.out.println(end);

            int[] length = new int[]{end - start};
            MPI.COMM_WORLD.Send(length, 0, 1, MPI.INT, process, 0);
            MPI.COMM_WORLD.Send(v1, start, end - start, MPI.INT, process, 0);
            MPI.COMM_WORLD.Send(v2, start, end - start, MPI.INT, process, 0);
        }

        int[] result = new int[size - 1];

        for (int process = 1; process < size; process++) {
            MPI.COMM_WORLD.Recv(result, process - 1 , 1, MPI.INT, process, 0);
        }

        int finalResult = combineResultsFromProcesses(result);

        System.out.println(finalResult);
    }

    public static void computeProdMPI(int me) {

        int[] length = new int[1];
        MPI.COMM_WORLD.Recv(length, 0, 1, MPI.INT, 0, 0);


        int[] p1 = new int[length[0]];
        int[] p2 = new int[length[0]];
        MPI.COMM_WORLD.Recv(p1, 0, length[0], MPI.INT, 0, 0);
        MPI.COMM_WORLD.Recv(p2, 0, length[0], MPI.INT, 0, 0);

        int[] result = computeProd(p1, p2);

        MPI.COMM_WORLD.Send(result, 0, 1, MPI.INT, 0, 0);
    }

    public static int[] computeProd(int[] p1, int[] p2) {
        int result = 0;

        for (int i = 0; i < p1.length; i++) {
            result += p1[i] * p2[i];
        }

        return new int[]{result};
    }
}
