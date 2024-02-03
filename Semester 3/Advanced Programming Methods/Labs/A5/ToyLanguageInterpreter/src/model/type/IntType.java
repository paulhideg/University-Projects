package model.type;

import model.value.Value;
import model.value.IntValue;

public class IntType implements Type {

    @Override
    public boolean equals(Type another) {

        return another instanceof IntType;
    }

    @Override
    public String toString() {
        return "int";
    }

    @Override
    public Type deepCopy() {
        return new IntType();
    }

    @Override
    public Value defaultValue() {
        return new IntValue(0);
    }

}


