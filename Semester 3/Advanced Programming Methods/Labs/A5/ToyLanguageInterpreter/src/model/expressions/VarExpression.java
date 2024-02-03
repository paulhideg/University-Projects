package model.expressions;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import model.type.Type;
import model.utils.MyIDict;
import model.utils.MyIHeap;
import model.value.Value;


public class VarExpression implements IExpression {
    private final String id;

    public VarExpression(String id) {
        this.id = id;
    }

    @Override
    public Type typecheck(MyIDict<String, Type> typeEnv) throws ExpressionEvalException, ADTException {
        return typeEnv.lookup(id);
    }


    @Override
    public Value eval(MyIDict<String, Value> symTable, MyIHeap heap) throws ExpressionEvalException, ADTException {
        return symTable.lookup(id);
    }

    @Override
    public  IExpression deepCopy() {
        return new VarExpression(id);
    }

    @Override
    public String toString() {
        return id;
    }
}

