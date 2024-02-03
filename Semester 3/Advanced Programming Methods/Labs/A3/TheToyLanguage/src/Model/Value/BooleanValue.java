package Model.value;

import model.type.Type;
import model.type.BooleanType;

public class BooleanValue implements Value {
    private final boolean value;

    public BooleanValue(boolean value) {
        this.value = value;
    }

    @Override
    public Type getType() {
        return new BooleanType();
    }

    @Override
    public boolean equals(Object another) {
        if (!(another instanceof BooleanValue))
            return false;
        BooleanValue castValue = (BooleanValue) another; //downcast from Object to BooleanValue
        return this.value == castValue.value;
    }

    @Override
    public Value deepCopy() {
        return new BooleanValue(value);
    }

    @Override
    public String toString() {
        return Boolean.toString(value);
    }

    public boolean getValue() {
        return value;
    }
}
