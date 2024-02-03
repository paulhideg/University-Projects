package model.statements;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import exceptions.StatementExecException;
import model.type.Type;
import model.utils.MyIDict;
import model.utils.MyIStack;
import model.programState.PrgState;

public class CompoundStmt implements IStmt {
    private IStmt first;
    private IStmt second;

    public CompoundStmt(IStmt first, IStmt second) {
        this.first = first;
        this.second = second;
    }

    @Override
    public MyIDict<String, Type> typecheck(MyIDict<String, Type> typeEnv) throws StatementExecException, ExpressionEvalException, ADTException {
        return second.typecheck(first.typecheck(typeEnv));
    }

    @Override
    public PrgState execute(PrgState state) throws StatementExecException, ExpressionEvalException, ADTException {
        MyIStack<IStmt> exeStack = state.getExeStack();
        exeStack.push(second);
        exeStack.push(first);
        state.setExeStack(exeStack);
        return null;
    }
    @Override
    public IStmt deepCopy() {
        return new CompoundStmt(first.deepCopy(), second.deepCopy());
    }

    @Override
    public String toString() {
        return "(" + first.toString() + ";" + second.toString() + ")";
    }
}

