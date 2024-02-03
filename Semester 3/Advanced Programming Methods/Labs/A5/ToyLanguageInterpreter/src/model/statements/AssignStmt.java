package model.statements;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import exceptions.StatementExecException;
import model.programState.PrgState;
import model.type.Type;
import model.value.Value;
import model.utils.MyIDict;
import model.expressions.IExpression;

public class AssignStmt implements IStmt {
    private final String id;
    private final IExpression exp;

    public AssignStmt(String id, IExpression exp) {
        this.id = id;
        this.exp = exp;
    }

    @Override
    public MyIDict<String, Type> typecheck(MyIDict<String, Type> typeEnv) throws StatementExecException, ExpressionEvalException, ADTException {
        Type typeVar = typeEnv.lookup(id);
        Type typeExp = exp.typecheck(typeEnv);
        if (typeVar.equals(typeExp))
            return typeEnv;
        else
            throw new StatementExecException("Assignment: right hand side and left hand side have different types");
    }


    @Override
    public PrgState execute(PrgState state) throws StatementExecException, ExpressionEvalException, ADTException {
        MyIDict<String, Value> symTable = state.getSymTable();
        if(symTable.isDefined(id)) {
            Value val = exp.eval(symTable, state.getHeap());
            Type typId = symTable.lookup(id).getType();
            if(val.getType().equals(typId))
                symTable.update(id, val);
            else
                throw new StatementExecException("Assignment: right hand side and left hand side have different types");
        }
        else
            throw new StatementExecException("Variable " + id + " is not defined");
        state.setSymTable(symTable);
        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new AssignStmt(id, exp.deepCopy());
    }

    @Override
    public String toString() {
        return id + " = " + exp.toString();
    }
}
