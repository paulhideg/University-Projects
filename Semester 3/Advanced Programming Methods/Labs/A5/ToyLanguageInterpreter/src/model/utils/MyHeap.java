package model.utils;
import exceptions.ADTException;
import model.utils.MyIHeap;
import model.value.Value;

import java.util.HashMap;
import java.util.Set;

public class MyHeap implements MyIHeap {

    HashMap<Integer, Value> heap;
    Integer freeLocation;

    public int newValue(){
        freeLocation++;
        while(heap.containsKey(freeLocation))
            freeLocation++;
        return freeLocation;
    }

    public MyHeap(){
        heap = new HashMap<>();
        freeLocation = 1;
    }

    @Override
    public int getFreeValue() {
        return freeLocation;
    }

    @Override
    public HashMap<Integer, Value> getContent() {
        return heap;
    }

    @Override
    public void setContent(HashMap<Integer, Value> newContent) {
        heap = newContent;
    }

    @Override
    public int add(Value value) {
        heap.put(freeLocation, value);
        Integer toReturn = freeLocation;
        freeLocation=newValue();
        return toReturn;
    }

    @Override
    public void update(Integer pos, Value value) throws ADTException {
        if (heap.containsKey(pos))
            heap.put(pos, value);
        else
            throw new ADTException("The position is not in the heap");
    }

    @Override
    public Value lookup(Integer pos) throws ADTException {
        if (heap.containsKey(pos))
            return heap.get(pos);
        else
            throw new ADTException("The position is not in the heap");
    }

    @Override
    public boolean isDefined(Integer pos) {
        return heap.containsKey(pos);
    }

    @Override
    public void remove(Integer key) throws ADTException {
        if(!heap.containsKey(key))
            throw new ADTException("The position is not in the heap");
        freeLocation = key;
        this.heap.remove(key);
    }

    @Override
    public Set<Integer> keySet() {
        return heap.keySet();
    }

    @Override
    public String toString(){
        return heap.toString();
    }
}
