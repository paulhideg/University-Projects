package model.expressions;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import model.type.RefType;
import model.utils.MyIDict;
import model.utils.MyIHeap;
import model.value.RefValue;
import model.value.Value;
import model.type.Type;

public class ReadHeapExpression implements IExpression{

    private final IExpression exp;

    public ReadHeapExpression(IExpression exp) {
        this.exp = exp;
    }

    @Override
    public Type typecheck(MyIDict<String, Type> typeEnv) throws ExpressionEvalException,ADTException {
        Type type = exp.typecheck(typeEnv);
        if (type instanceof RefType) {
            RefType refType = (RefType) type;
            return refType.getInner();
        } else {
            throw new ExpressionEvalException("The rH argument is not a Ref Type");
        }
    }


    @Override
    public Value eval(MyIDict<String, Value> symTable, MyIHeap heap) throws ExpressionEvalException, ADTException {
        Value value = exp.eval(symTable, heap);

        if(!(value instanceof RefValue))
            throw new ExpressionEvalException("The value is not a reference value");

        int address = ((RefValue) value).getAddress();

        if(!heap.isDefined(address))
            throw new ExpressionEvalException("The address is not a key in the heap");

        return heap.lookup(address);
    }

    @Override
    public IExpression deepCopy() {
        return new ReadHeapExpression(exp.deepCopy());
    }

    @Override
    public String toString() {
        return "rH(" + exp + ")";
    }
}
