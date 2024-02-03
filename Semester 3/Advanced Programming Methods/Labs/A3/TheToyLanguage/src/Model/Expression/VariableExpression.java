package Model.Expression;

import Collection.Dictionary.MyIDictionary;
import Exception.ToyLanguageInterpreterException;
import Model.Value.Value;

public class VariableExpression implements  IExpression{
    String key;

    public VariableExpression(String key){
        this.key = key;
    }

    @Override
    public Value evaluate(MyIDictionary<String, Value> symbolTable) throws ToyLanguageInterpreterException {
        return symbolTable.get(key);
    }

    @Override
    public String toString(){
        return key;
    }
}
