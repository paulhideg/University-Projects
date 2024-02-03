package model.expressions;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import model.type.Type;
import model.utils.MyIDict;
import model.utils.MyIHeap;
import model.value.Value;
import model.value.BooleanValue;
import model.type.BooleanType;

public class LogicExpression implements IExpression{
    private IExpression e1;
    private IExpression e2;
    private String op;

    public LogicExpression(IExpression e1, IExpression e2, String op) {
        this.e1 = e1;
        this.e2 = e2;
        this.op = op;
    }


    @Override

    public Type typecheck(MyIDict<String, Type> typeEnv) throws ExpressionEvalException, ADTException {
        Type type1, type2;
        type1 = e1.typecheck(typeEnv);
        type2 = e2.typecheck(typeEnv);
        if (type1.equals(new BooleanType())) {
            if (type2.equals(new BooleanType())) {
                return new BooleanType();
            } else {
                throw new ExpressionEvalException("second operand is not a boolean");
            }
        } else {
            throw new ExpressionEvalException("first operand is not a boolean");
        }
    }


    @Override
    public Value eval(MyIDict<String, Value> symTable, MyIHeap heap) throws ExpressionEvalException, ADTException {
        Value v1, v2;
        v1 = e1.eval(symTable, heap);
        if (v1.getType().equals(new BooleanType())) {
            v2 = e2.eval(symTable, heap);
            if (v2.getType().equals(new BooleanType())) {
                BooleanValue i1 = (BooleanValue) v1;
                BooleanValue i2 = (BooleanValue) v2;
                boolean n1, n2;
                n1 = i1.getValue();
                n2 = i2.getValue();
                if (op.equals("and"))
                    return new BooleanValue(n1 && n2);
                if (op.equals("or"))
                    return new BooleanValue(n1 || n2);
            } else
                throw new ExpressionEvalException("Second operand is not a boolean");
        } else
            throw new ExpressionEvalException("First operand is not a boolean");
        return null;
    }

    @Override
    public IExpression deepCopy() {
        return new LogicExpression(e1.deepCopy(), e2.deepCopy(), op);
    }

    @Override
    public String toString() {
        return e1.toString() + op + e2.toString();
    }

}
