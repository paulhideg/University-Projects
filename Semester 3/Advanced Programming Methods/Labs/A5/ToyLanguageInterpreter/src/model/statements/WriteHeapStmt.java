package model.statements;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import exceptions.StatementExecException;
import model.expressions.IExpression;
import model.programState.PrgState;
import model.type.RefType;
import model.type.Type;
import model.utils.MyDict;
import model.utils.MyIDict;
import model.utils.MyIHeap;
import model.value.RefValue;
import model.value.Value;

public class WriteHeapStmt implements IStmt {
    private final String varName;
    private final IExpression exp;

    public WriteHeapStmt(String varName, IExpression exp) {
        this.varName = varName;
        this.exp = exp;
    }

    @Override
    public PrgState execute(PrgState state) throws StatementExecException, ExpressionEvalException, ADTException {
        MyIDict<String, Value> symTable = state.getSymTable();
        MyIHeap heap = state.getHeap();

        if (!symTable.isDefined(varName))
            throw new StatementExecException("Variable " + varName + " is not defined");

        Value varValue = symTable.lookup(varName);
        if (!(varValue instanceof RefValue))
            throw new StatementExecException("Variable " + varName + " is not a reference");

        int address = ((RefValue) varValue).getAddress();
        if (!heap.isDefined(address))
            throw new StatementExecException("Address " + address + " is not defined in the heap");

        Value expValue = exp.eval(symTable, heap);
        if (!expValue.getType().equals(((RefValue) varValue).getLocationType()))
            throw new StatementExecException("Type of " + expValue + " does not match type of " + heap.lookup(address));

        heap.update(address, expValue);
        state.setHeap(heap);

        return null;
    }

    @Override
    public MyIDict<String, Type> typecheck(MyIDict<String, Type> typeEnv) throws StatementExecException, ExpressionEvalException, ADTException {
        Type typeVar = typeEnv.lookup(varName);
        Type typeExp = exp.typecheck(typeEnv);
        if(typeVar.equals(new RefType(typeExp)))
            return typeEnv;
        else
            throw new StatementExecException("WritHeapt: right hand side and left hand side have different types");
    }


    @Override
    public IStmt deepCopy() {
        return new WriteHeapStmt(varName, exp.deepCopy());
    }

    @Override
    public String toString() {
        return "wH(" + varName + ", " + exp + ")";
    }
}

