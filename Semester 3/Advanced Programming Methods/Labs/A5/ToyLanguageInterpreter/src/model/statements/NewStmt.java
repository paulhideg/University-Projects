package model.statements;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import exceptions.StatementExecException;
import model.expressions.IExpression;
import model.programState.PrgState;
import model.type.RefType;
import model.type.Type;
import model.utils.MyIDict;
import model.utils.MyIHeap;
import model.value.RefValue;
import model.value.Value;

import java.sql.Ref;

public class NewStmt implements IStmt{

    private final String varName;

    private final IExpression exp;

    public NewStmt(String varName, IExpression exp){
        this.varName = varName;
        this.exp = exp;
    }

    @Override
    public MyIDict<String, Type> typecheck(MyIDict<String, Type> typeEnv) throws StatementExecException, ExpressionEvalException, ADTException {
        Type typeVar = typeEnv.lookup(varName);
        Type typeExp = exp.typecheck(typeEnv);
        if(typeVar.equals(new RefType(typeExp)))
            return typeEnv;
        else
            throw new StatementExecException("NewStmt: right hand side and left hand side have different types");
    }

    @Override
    public PrgState execute(PrgState state) throws StatementExecException, ExpressionEvalException, ADTException{
        MyIDict<String, Value> symTable = state.getSymTable();
        MyIHeap heap = state.getHeap();

        if(!symTable.isDefined(varName))
            throw  new StatementExecException("variable not in symTable");

        Value varValue = symTable.lookup(varName);
        if(!(varValue.getType() instanceof RefType))
            throw new StatementExecException("variable is not of refType");

        Value evaluated = exp.eval(symTable,heap);
        Type locationType = ((RefValue)varValue).getLocationType();

        if(!locationType.equals(evaluated.getType()))
            throw new StatementExecException((String.format("%s not of %s", varName, evaluated.getType())));

        int newPos= heap.add(evaluated);
        symTable.put(varName, new RefValue(newPos,locationType));
        state.setSymTable(symTable);
        state.setHeap(heap);

        return null;
    }

    @Override
    public IStmt deepCopy() {
        return new NewStmt(varName, exp.deepCopy());
    }

    @Override
    public String toString(){
        return String.format("new(%s, %s)", varName, exp.toString());
    }
}
