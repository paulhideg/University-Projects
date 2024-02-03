package Model.Value;

import Model.Type.Type;
import Model.Type.StringType;

public class StringValue implements Value {
    private final String value;

    public StringValue(String value) {
        this.value = value;
    }

    @Override
    public String toString() {
        return value;
    }

    @Override
    public boolean equals(Object anotherValue) {
        if (!(anotherValue instanceof StringValue))
            return false;
        StringValue castValue = (StringValue) anotherValue;
        return this.value.equals(castValue.value);
    }

    @Override
    public Value deepCopy() {
        return new StringValue(value);
    }

    @Override
    public Type getType() {
        return new StringType();
    }

    public String getValue() {
        return value;
    }
}