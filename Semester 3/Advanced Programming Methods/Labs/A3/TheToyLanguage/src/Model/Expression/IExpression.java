package Model.Expression;

import Collection.Dictionary.MyIDictionary;
import Exception.ToyLanguageInterpreterException;
import Model.Value.Value;

import java.io.FileNotFoundException;

public interface IExpression {
    Value evaluate(MyIDictionary<String, Value> symbolTable) throws ToyLanguageInterpreterException;
    String toString();
}
