package org.example;

import mpi.MPI;

import java.util.Arrays;

public class Y2023no2 {

    private static int combineResultsFromProcesses(int[] polynomials) {

        int result = 0;
        for (int polynomial : polynomials) {
            result += polynomial;
        }

        return result;
    }
    public static void initializeMPI(int[][] matrix, int size) {

        int chunkSize = matrix.length / (size - 1);
        for (int process = 1; process < size; process++) {

            int start = chunkSize * (process - 1);
            int end;
            if(process == size - 1){
                end = matrix.length;
            } else {
                end = start + chunkSize ;
            }

            int[] length = new int[]{end - start};
            MPI.COMM_WORLD.Send(length, 0, 1, MPI.INT, process, 0);

            int vLength = matrix[0].length;
            int[] vectorLength = new int[]{vLength};
            MPI.COMM_WORLD.Send(vectorLength, 0, 1, MPI.INT, process, 0);

            for(int i = start; i < end; i++){
                MPI.COMM_WORLD.Send(matrix[i], 0, vLength, MPI.INT, process, 0);
            }
        }

        int[] result = new int[size - 1];

        for (int process = 1; process < size; process++) {
            MPI.COMM_WORLD.Recv(result, process - 1 , 1, MPI.INT, process, 0);
        }

        int finalResult = combineResultsFromProcesses(result);

        System.out.println(finalResult);
    }

    public static void computeSumMPI(int me) {

        int[] length = new int[1];
        MPI.COMM_WORLD.Recv(length, 0, 1, MPI.INT, 0, 0);

        int[] vectorLength = new int[1];
        MPI.COMM_WORLD.Recv(vectorLength, 0, 1, MPI.INT, 0, 0);

        int[][] matrix = new int[length[0]][vectorLength[0]];
        for(int i=0; i < length[0]; i++){
            int[] p1 = new int[vectorLength[0]];
            MPI.COMM_WORLD.Recv(p1, 0, vectorLength[0], MPI.INT, 0, 0);
            matrix[i] = p1;
        }

        int[] result = computeSumMatrix(matrix);

        MPI.COMM_WORLD.Send(result, 0, 1, MPI.INT, 0, 0);
    }

    private static int[] computeSumMatrix(int[][] matrix) {
        int result = 0;
        for (int[] ints : matrix) {
            result += computeSumVector(ints);
        }

        return new int[]{result};
    }

    private static int computeSumVector(int[] vector){
        int result = 0;
        for (int j : vector) {
            result += j;
        }
        return result;
    }
}
