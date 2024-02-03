package Model.Statement;

import Exception.ToyLanguageInterpreterException;
import Model.State.ProgramState;
import Model.Type.IntType;
import Model.Type.StringType;
import Model.Value.IntValue;
import Model.Value.StringValue;
import Model.Value.Value;

import Model.Expression.IExpression;
import java.io.*;

public class ReadFileStatement implements IStatement{

    private final IExpression expression;
    private final String var;

    public ReadFileStatement(IExpression expression, String var){
        this.expression = expression;
        this.var = var;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageInterpreterException, IOException {

        if(state.getSymbolTable().isDefined(var)) {
            if(state.getSymbolTable().lookup(var).getType().equals(new IntType())){
                Value evalValue;
                evalValue = this.expression.evaluate(state.getSymbolTable());
                if(evalValue.getType().equals(new StringType())){
                    StringValue downValue = (StringValue) evalValue;
                    String expValue = downValue.getValue();
                    if(state.getFileTable().isDefined(expValue)){
                        BufferedReader fileDesc = state.getFileTable().lookup(expValue);
                        String line = fileDesc.readLine();
                        IntValue readValue;
                        if(line == null)
                            readValue = new IntValue(0);
                        else
                            readValue = new IntValue(Integer.parseInt(line));
                        state.getSymbolTable().update(this.var, readValue);
                    }
                    else
                        throw new ToyLanguageInterpreterException("No entry in file table!");
                }
                else
                    throw new ToyLanguageInterpreterException("Expression not a string");
            }
            else
                throw new ToyLanguageInterpreterException("Value type is not int");
        }
        else
            throw new ToyLanguageInterpreterException("Variable name not defined in symbol table");
        return null;
    }

    @Override
    public String toString() {
        return "read(" + this.expression.toString() + ";" + this.var + ")";
    }
}
