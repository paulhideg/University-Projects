package model.type;
import model.value.StringValue;

public class StringType implements Type {

    @Override
    public boolean equals(Type another) {
        return another instanceof StringType;
    }

    @Override
    public String toString() {
        return "string";
    }

    @Override
    public Type deepCopy() {
        return new StringType();
    }

    @Override
    public StringValue defaultValue() {
        return new StringValue("");
    }
}

