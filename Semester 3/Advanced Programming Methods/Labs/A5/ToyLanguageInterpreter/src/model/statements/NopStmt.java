package model.statements;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import exceptions.StatementExecException;
import model.programState.PrgState;
import model.type.Type;
import model.utils.MyIDict;

public class NopStmt implements IStmt {


    @Override
    public PrgState execute(PrgState state) throws StatementExecException, ExpressionEvalException, ADTException {
        return null;
    }

    @Override
    public MyIDict<String, Type> typecheck(MyIDict<String, Type> typeEnv) throws StatementExecException, ExpressionEvalException, ADTException {
        return typeEnv;
    }

    @Override
    public IStmt deepCopy() {
        return new NopStmt();
    }
    @Override
    public String toString() {
        return "nop";
    }
}
