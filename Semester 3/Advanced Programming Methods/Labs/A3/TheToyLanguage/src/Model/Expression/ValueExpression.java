package Model.Expression;

import Collection.Dictionary.MyIDictionary;
import Model.Value.Value;


public class ValueExpression implements IExpression{
    Value value;

    public ValueExpression(Value value) {
        this.value = value;
    }

    @Override
    public Value evaluate(MyIDictionary<String, Value> symbolTable){
        return this.value;
    }

    @Override
    public String toString(){return this.value.toString();}
}
