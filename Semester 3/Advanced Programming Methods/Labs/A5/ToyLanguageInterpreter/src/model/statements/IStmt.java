package model.statements;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import exceptions.StatementExecException;
import model.programState.PrgState;
import model.type.Type;
import model.utils.MyIDict;

public interface IStmt {
    PrgState execute(PrgState state) throws StatementExecException, ExpressionEvalException, ADTException;
    IStmt deepCopy();
    MyIDict<String, Type> typecheck(MyIDict<String, Type> typeEnv) throws StatementExecException, ExpressionEvalException, ADTException;
}
