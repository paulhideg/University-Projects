package Model.Expression;

import Collection.Dictionary.MyIDictionary;
import Exception.DivisionByZeroException;
import Exception.ToyLanguageInterpreterException;
import Exception.VariableException;
import Model.Type.IntType;
import Model.Value.IntValue;
import Model.Value.Value;

public class ArithmeticExpression implements IExpression {
    private final IExpression expression1;
    private final IExpression expression2;

    char operation;

    public ArithmeticExpression(char operation, IExpression expression1, IExpression expression2){
        this.expression1 = expression1;
        this.expression2 = expression2;
        this.operation = operation;
    }

    @Override
    public Value evaluate(MyIDictionary<String,Value> symbolTable) throws ToyLanguageInterpreterException {
        Value value1, value2;
        value1 = this.expression1.evaluate(symbolTable);

        if (value1.getType().equals(new IntType())){
            value2 = this.expression2.evaluate(symbolTable);
            if (value2.getType().equals(new IntType())){
                IntValue int1 = (IntValue) value1;
                IntValue int2 = (IntValue) value2;

                int n1,n2;
                n1 = int1.getValue();
                n2 = int2.getValue();

                if (this.operation == '+'){
                    return new IntValue(n1+n2);
                }
                else if (this.operation == '-'){
                    return new IntValue(n1-n2);
                }
                else if (this.operation == '*'){
                    return new IntValue(n1*n2);
                }
                else if (this.operation == '/'){
                    if (n2 == 0){
                        throw new DivisionByZeroException("Division by zero!");
                    }
                    else {
                        return new IntValue(n1 / n2);
                    }
                }

            }
            else {
                throw new VariableException("Second operand is not an integer!");
            }
        }
        else {
            throw new VariableException("First operand is not an integer!");
        }
        return null;
    }

    @Override
    public String toString(){
        return this.expression1.toString() + " " + this.operation + " " + this.expression2.toString();
    }
}
