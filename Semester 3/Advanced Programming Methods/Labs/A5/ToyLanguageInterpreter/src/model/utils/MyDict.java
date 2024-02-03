package model.utils;

import exceptions.ADTException;

import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

public class MyDict<K,V> implements MyIDict<K,V>{

    private HashMap<K,V> dict;

    public MyDict(){
        this.dict=new HashMap<>();
    }

    @Override
    public boolean isDefined(K key){
        return dict.containsKey(key);
    }

    @Override
    public V lookup(K key) throws ADTException{
        if(!isDefined(key))
            throw new ADTException(key + " is not defined");
        return dict.get(key);
    }

    @Override
    public void put(K key, V value){
        this.dict.put(key,value);
    }

    @Override
    public void update(K key, V value) throws ADTException{
        if(!isDefined(key))
            throw new ADTException(key+ " is not defined");
        this.dict.put(key,value);
    }

    @Override
    public void remove(K key) throws ADTException{
        if(!isDefined(key))
            throw new ADTException(key+ " is not defined");
        this.dict.remove(key);
    }

    @Override
    public Collection<V> values(){
        return this.dict.values();
    }

    @Override
    public Map<K,V> getContent(){
        return dict;
    }

    @Override
    public String toString(){
        return dict.toString();
    }

    @Override
    public MyIDict<K, V> deepCopy() throws ADTException {
        MyIDict<K, V> newDict = new MyDict<>();
        for (Map.Entry<K, V> entry : dict.entrySet()) {
            newDict.put(entry.getKey(), entry.getValue());
        }
        return newDict;
    }
}
