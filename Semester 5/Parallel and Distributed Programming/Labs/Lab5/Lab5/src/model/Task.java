package model;

public final class Task implements Runnable {
    private final int start;
    private final int end;
    private final Polynomial p1;
    private final Polynomial p2;
    private final Polynomial result;

    public Task(int start, int end, Polynomial p1, Polynomial p2, Polynomial result) {
        this.start = start;
        this.end = end;
        this.p1 = p1;
        this.p2 = p2;
        this.result = result;
    }

    @Override
    public void run() {
        // Iterate through the specified range of coefficients in the result polynomial
        for (int index = start; index < end; index++) {
            // Case - no more elements to calculate
            if (index > result.getLength()) {
                return;
            }
            // Find all pairs that contribute to the value of a result coefficient
            for (int j = 0; j <= index; j++) {
                // Check if the indices are within the bounds of the input polynomials
                if (j < p1.getLength() && (index - j) < p2.getLength()) {
                    // Multiply the corresponding coefficients and add to the result
                    int value = p1.getCoefficients().get(j) * p2.getCoefficients().get(index - j);
                    result.getCoefficients().set(index, result.getCoefficients().get(index) + value);
                }
            }
        }
    }
}