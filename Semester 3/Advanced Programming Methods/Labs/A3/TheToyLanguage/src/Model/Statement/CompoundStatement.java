package Model.Statement;

import Collection.Stack.MyIStack;
import Exception.ToyLanguageInterpreterException;
import Model.State.ProgramState;

public class CompoundStatement implements IStatement {
    private final IStatement first;
    private final IStatement second;

    public CompoundStatement(IStatement first, IStatement second){
        this.first = first;
        this.second = second;
    }

    @Override
    public ProgramState execute(ProgramState state) {
        MyIStack<IStatement> stack = state.getExecutionStack();
        stack.push(this.second);
        stack.push(this.first);
        state.setExecutionStack(stack);
        return state;
    }

    @Override
    public String toString(){
        return this.first.toString() + "; " + this.second.toString();
    }
}
