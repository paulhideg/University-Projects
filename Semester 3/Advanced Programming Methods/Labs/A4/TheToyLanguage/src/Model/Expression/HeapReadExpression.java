package Model.Expression;

import Exception.ToyLanguageInterpreterException;
import Collection.Dictionary.MyIDictionary;
import Collection.Heap.MyIHeap;
import Model.Value.RefValue;
import Model.Value.Value;

public class HeapReadExpression implements IExpression{

    private final IExpression exp;

    public HeapReadExpression(IExpression exp){
        this.exp = exp;
    }

    @Override
    public Value evaluate(MyIDictionary<String, Value> symbolTable, MyIHeap<Value> heapTable) throws ToyLanguageInterpreterException {

        Value evalValue = this.exp.evaluate(symbolTable, heapTable);
        if(evalValue instanceof RefValue){
            int addr = ((RefValue) evalValue).getAddress();
            Value valueFromHeap = heapTable.get(addr);
            if(valueFromHeap != null){
                return valueFromHeap;
            }
            else
                throw new ToyLanguageInterpreterException("Address doesn't have a value");
        }
        else
            throw new ToyLanguageInterpreterException("Value is not of type reference value");
    }

    @Override
    public String toString(){
        return "rH(" + this.exp.toString() + ")";
    }
}
