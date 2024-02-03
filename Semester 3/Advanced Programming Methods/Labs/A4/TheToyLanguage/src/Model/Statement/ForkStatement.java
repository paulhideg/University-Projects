package Model.Statement;

import Collection.Stack.MyStack;
import Model.State.ProgramState;
import Exception.ToyLanguageInterpreterException;
import java.io.IOException;

public class ForkStatement implements IStatement{

    private IStatement statement;

    public ForkStatement(IStatement statement){
        this.statement = statement;
    }

    public IStatement getStatement() {
        return statement;
    }

    public void setStatement(IStatement statement) {
        this.statement = statement;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageInterpreterException, IOException {
        return new ProgramState(new MyStack<>(), state.getSymbolTable().clone_dict(), state.getOutputList(),
                this.statement, state.getHeap(), state.getFileTable());
    }

    @Override
    public String toString() {
        return "fork(" + this.statement.toString() + ")";
    }
}
