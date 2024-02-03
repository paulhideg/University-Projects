package ro.paulhideg.utils;

import ro.paulhideg.model.Matrix;
import ro.paulhideg.model.MatrixException;
import ro.paulhideg.thread.ColumnTask;
import ro.paulhideg.thread.KTask;
import ro.paulhideg.thread.MatrixTask;
import ro.paulhideg.thread.RowTask;

public final class Utils {

    //inmulteste elementele din randul i din a cu elementele din coloana j din b,
    public static int buildElement(Matrix a, Matrix b, int i, int j) throws MatrixException {
        if (i<a.n && j<b.m){
            int element = 0;
            for (int k=0;k<a.m;k++){
                element+=a.get(i,k) * b.get(k,j);
            }
            return element;
        }
        else
            throw new MatrixException("Row/column out of bounds!");
    }

    public static MatrixTask initRowThread(int index, Matrix a, Matrix b, Matrix c, int noThreads) {
        int resultSize = c.n * c.m;
        int count = resultSize / noThreads;

        int iStart = count * index / c.n;
        int jStart = count * index % c.n;

        if (index == noThreads - 1)
            count += resultSize % noThreads;

        return new RowTask(iStart, jStart, count, a, b, c);
    }

    public static MatrixTask initColThread(int index, Matrix a, Matrix b, Matrix c, int noThreads) {
        int resultSize = c.n * c.m;
        int count = resultSize / noThreads;

        int iStart = count * index % c.n;
        int jStart = count * index / c.n;

        if (index == noThreads - 1)
            count += resultSize % noThreads;

        return new ColumnTask(iStart, jStart, count, a, b, c);
    }

    public static MatrixTask initKThread(int index, Matrix a, Matrix b, Matrix c, int noThreads) {
        int resultSize = c.n * c.m;
        int count = resultSize/noThreads;

        if (index < resultSize % noThreads)
            count++;

        int iStart = index / c.m;
        int jStart = index % c.m;
        return new KTask(iStart, jStart, count, noThreads, a, b, c);
    }


}