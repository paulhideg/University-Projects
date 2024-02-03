package model.utils;

import exceptions.ADTException;
import java.util.Stack;

public class MyStack <T> implements MyIStack<T> {
    private Stack<T> stack;

    public MyStack() {
        stack = new Stack<>();
    }

    @Override
    public T pop() throws ADTException {
        if(stack.isEmpty())
            throw new ADTException("Stack is empty");
        return stack.pop();
    }

    @Override
    public void push(T v) {
        stack.push(v);
    }

    @Override
    public T peek() {
        return stack.peek();
    }

    @Override
    public boolean isEmpty() {
        return stack.isEmpty();
    }

    @Override
    public String toString() {
        return stack.toString();
    }
}
