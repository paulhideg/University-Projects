package exam;

import java.util.ArrayList;
import java.util.List;

public class Animals {
    public List<Integer> findPair(List<Integer> animals, int startIndex) {
        for (int i = startIndex; i < animals.size() - 1; i++) {
            if ((animals.get(i) == 1 && animals.get(i + 1) == 2) ||
                    (animals.get(i) == 2 && animals.get(i + 1) == 1) ||
                        (animals.get(i) == 2 && animals.get(i + 1) == 3) ||
                            (animals.get(i) == 3 && animals.get(i + 1) == 2)) {
                ArrayList<Integer> pair = new ArrayList<>();
                pair.add(i);
                pair.add(i + 1);
                return pair;
            }
        }
        return null;
    }

    public void insertCow(List<Integer> animals, int index) {
        if (index < 0 || index >= animals.size()) {
            throw new IllegalArgumentException("Index out of bounds");
        }
        animals.add(index + 1, 4);
    }

    public List<Integer> beFriends(List<Integer> animals) {
        int startIndex = 0;
        while (true) {
            List<Integer> pair = findPair(animals, startIndex);
            if (pair == null) {
                break;
            }
            insertCow(animals, pair.get(0));
            startIndex = pair.get(1) + 1;
        }
        return animals;
    }
}
