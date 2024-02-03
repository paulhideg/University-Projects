package model.value;

import model.type.Type;
import model.type.IntType;

public class IntValue implements Value{
    private final int value;

    public IntValue(int value){
        this.value = value;
    }

    @Override
    public Type getType() {
        return new IntType();
    }

    @Override
    public boolean equals(Object another){
        if(!(another instanceof IntValue))
            return false;
        IntValue castValue = (IntValue) another; //downcast from Object to IntValue
        return this.value == castValue.value;
    }

    @Override
    public Value deepCopy() {
        return new IntValue(value);
    }

    @Override
    public String toString(){
        return Integer.toString(value);
    }

    public int getValue(){
        return value;
    }
}
