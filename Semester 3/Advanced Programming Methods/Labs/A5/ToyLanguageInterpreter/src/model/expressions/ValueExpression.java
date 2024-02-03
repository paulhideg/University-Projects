package model.expressions;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import model.type.Type;
import model.utils.MyIDict;
import model.utils.MyIHeap;
import model.value.Value;

public class ValueExpression implements IExpression {
    private final Value value;

    public ValueExpression(Value value) {
        this.value = value;
    }

    @Override
    public Type typecheck(MyIDict<String, Type> typeEnv) throws ExpressionEvalException, ADTException {
        return value.getType();
    }


    @Override
    public Value eval(MyIDict<String, Value> symTable, MyIHeap heap) throws ExpressionEvalException, ADTException {
        return value;
    }

    @Override
    public IExpression deepCopy() {
        return new ValueExpression(value);
    }
    
    @Override
    public String toString() {
        return value.toString();
    }
}

