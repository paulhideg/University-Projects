package Model.Statement;

import Collection.Dictionary.MyIDictionary;
import Exception.StatementExecutionException;
import Exception.ToyLanguageInterpreterException;
import Model.Expression.IExpression;
import Model.State.ProgramState;
import Model.Type.Type;
import Model.Value.Value;

public class AssignStatement implements IStatement{

    private final String key;

    private final IExpression expression;

    public AssignStatement(String key, IExpression expression){
        this.key = key;
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageInterpreterException {
        MyIDictionary<String, Value> symbolTable = state.getSymbolTable();

        if (symbolTable.containsKey(this.key)){
            Value value = this.expression.evaluate(symbolTable);
            Type typeId = (symbolTable.get(this.key)).getType();

            if (value.getType().toString().equals(typeId.toString())){
                symbolTable.put(this.key,value);
            }
            else{
                throw new StatementExecutionException("Declared type of variable " + this.key + " and type of the assigned expression do not match.");
            }
        }
        else{
            throw new StatementExecutionException("The used variable " + this.key + " isn't declared.");
        }
        state.setSymbolTable(symbolTable);
        return state;
    }

    @Override
    public String toString(){
        return this.key + " = " + this.expression.toString();
    }

}
