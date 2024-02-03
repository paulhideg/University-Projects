package Collection.Stack;

import Exception.ADTEmptyException;

public interface MyIStack<T> {
    T pop() throws ADTEmptyException;
    void push(T v);
    boolean isEmpty();
    String toString();

    int size();

}
