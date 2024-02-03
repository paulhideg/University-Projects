package ro.paulhideg;

import ro.paulhideg.model.Matrix;
import ro.paulhideg.model.MatrixException;
import ro.paulhideg.runner.NormalThreadRunner;
import ro.paulhideg.runner.ThreadPoolRunner;

public class Main {

    private static final int n1=1000;
    private static final int m1=1000;
    private static final int n2=1000;
    private static final int m2=1000;

    private static final int NO_THREADS = 500;
    private static final String APPROACH = "Normal";//Pool Normal
    private static final String FUNCTION = "Row"; //Row Column Kth

    public static void main(String[] args) {
        // write your code here

        Matrix a = new Matrix(n1, m1);
        Matrix b = new Matrix(n2, m2);

        a.populate();
        b.populate();

        System.out.println(a);
        System.out.println(b);

        if (a.m == b.n){
            Matrix result = new Matrix(a.n, b.m);
            float start = System.nanoTime() / 1_000_000;
            if (APPROACH.equals("Pool")){
                try {
                    ThreadPoolRunner.run(a,b,result, NO_THREADS, FUNCTION);
                } catch (MatrixException e) {
                    System.err.println(e.getMessage());
                }
            }
            else if (APPROACH.equals("Normal")){
                try {
                    NormalThreadRunner.run(a,b,result, NO_THREADS, FUNCTION);
                } catch (MatrixException e) {
                    System.err.println(e.getMessage());
                }
            }
            else {
                System.err.println("Invalid approach.");
            }
            float end = System.nanoTime() / 1_000_000;

            System.out.println("Time elapsed: " + (end-start)/1000 + " seconds");

        }
        else{
            System.err.println("The matrices can't be multiplied");
        }
    }

}