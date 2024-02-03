package model.utils;

import exceptions.ADTException;

public interface MyIStack <T> {
    T pop() throws ADTException;
    void push(T v);
    T peek();
    boolean isEmpty();
    String toString();
}
