package model.type;

import model.value.RefValue;
import model.value.Value;

public class RefType implements Type {
    private Type inner;

    public RefType(Type inner) {
        this.inner = inner;
    }

    public Type getInner() {
        return inner;
    }

    @Override
    public boolean equals(Type another) {
        if (another instanceof RefType) {
            return inner.equals(((RefType) another).getInner());
        }
        return false;
    }

    @Override
    public Type deepCopy() {
        return new RefType(inner.deepCopy());
    }

    @Override
    public String toString() {
        return "Ref(" + inner + ")";
    }

    @Override
    public Value defaultValue() {
        return new RefValue(0, inner);
    }
}
