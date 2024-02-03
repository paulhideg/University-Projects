package model.utils;

import exceptions.ADTException;
import model.value.Value;

import java.util.HashMap;
import java.util.Set;

public interface MyIHeap {
    int getFreeValue();
    HashMap<Integer, Value> getContent();
    void setContent(HashMap<Integer, Value> newContent);
    int add(Value value);
    void update(Integer pos, Value value)throws ADTException;
    Value lookup(Integer pos) throws ADTException;
    boolean isDefined(Integer pos);
    void remove(Integer key)throws ADTException;
    Set<Integer> keySet();
}
