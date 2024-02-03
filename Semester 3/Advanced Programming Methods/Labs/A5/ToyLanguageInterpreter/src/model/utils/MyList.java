package model.utils;

import exceptions.ADTException;
import java.util.List;
import java.util.ArrayList;

public class MyList<T> implements MyIList<T> {
    private List<T> list;

    public MyList() {
        this.list = new ArrayList<>();
    }

    @Override
    public void add(T elem) {
        list.add(elem);
    }

    @Override
    public T pop() throws ADTException {
        if(list.isEmpty())
            throw new ADTException("List is empty");
        return list.remove(0);
    }

    @Override
    public boolean isEmpty() {
        return list.isEmpty();
    }

    @Override
    public List<T> getAll() {
        return list;
    }

    @Override
    public String toString(){
        return list.toString();
    }
}
