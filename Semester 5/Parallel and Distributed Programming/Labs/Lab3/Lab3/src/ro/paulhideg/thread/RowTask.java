package ro.paulhideg.thread;

import ro.paulhideg.model.Matrix;
import ro.paulhideg.model.Pair;


public final class RowTask extends MatrixTask {

    public RowTask(int iStart, int jStart, int count, Matrix a, Matrix b, Matrix result) {
        super(iStart, jStart, count, a, b, result);

    }

    //in ce ordine se calculeaza fiecare element din matricea finala in functie de ce tip de task e
    //se da increase la j pana cand numarul size-ului unui task e 0
    public void computeElements() {
        int i = iStart, j = jStart;
        int size = sizeOfTask;
        while (size > 0 && i < result.n && j<result.m) {
            pairs.add(new Pair<>(i, j));
            j++;
            size--;
            if (j == result.n) {
                j = 0;
                i++;
            }
        }
    }
}