package model.utils;

import java.util.Collection;
import java.util.Map;
import exceptions.ADTException;

public interface MyIDict <K, V> {
    V lookup(K key) throws ADTException;
    void put(K key, V value);
    void update(K key, V value) throws ADTException;
    boolean isDefined(K key);
    Collection<V> values();
    void remove(K key) throws ADTException;
    Map<K, V> getContent();

    MyIDict<K, V> deepCopy() throws ADTException;
}
