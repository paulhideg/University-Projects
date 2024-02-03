package Model.Statement;

import Exception.ToyLanguageInterpreterException;
import Model.State.ProgramState;
import Model.Type.StringType;
import Model.Value.StringValue;
import Model.Value.Value;

import Model.Expression.IExpression;
import java.io.*;

public class CloseFileStatement implements IStatement{

    private final IExpression expression;

    public CloseFileStatement(IExpression expression){
        this.expression = expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageInterpreterException, IOException {
        Value evalValue;
        evalValue = this.expression.evaluate(state.getSymbolTable());
        if(evalValue.getType().equals(new StringType())){
            StringValue downValue = (StringValue) evalValue;
            String expValue = downValue.getValue();
            if(state.getFileTable().isDefined(expValue)){
                BufferedReader fileDesc = state.getFileTable().get(expValue);
                fileDesc.close();
                state.getFileTable().delete(expValue);
            }
            else
                throw new ToyLanguageInterpreterException("File name doesn't exist!");
        }
        else
            throw new ToyLanguageInterpreterException("Expression is not a string");
        return null;
    }

    @Override
    public String toString(){
        return "close(" + this.expression.toString() + ")";
    }
}
