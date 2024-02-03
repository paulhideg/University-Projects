package Model.Statement;

import Collection.List.MyIList;
import Exception.ToyLanguageInterpreterException;
import Model.Expression.IExpression;
import Model.State.ProgramState;
import Model.Value.Value;

public class PrintStatement implements IStatement{
    private final IExpression expression;

    public PrintStatement(IExpression expression){
        this.expression=expression;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageInterpreterException{
        MyIList<Value> out = state.getOutputList();
        out.add(this.expression.evaluate(state.getSymbolTable()));
        state.setOutputList(out);
        return state;
    }

    @Override
    public String toString(){
        return String.format("Print(%s)", this.expression.toString());
    }
}
