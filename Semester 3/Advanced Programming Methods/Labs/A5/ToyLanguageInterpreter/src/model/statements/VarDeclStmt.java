package model.statements;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import exceptions.StatementExecException;
import model.programState.PrgState;
import model.type.Type;
import model.utils.MyIDict;
import model.value.Value;

public class VarDeclStmt implements IStmt{

    String name;
    Type type;

    public VarDeclStmt(String name, Type type){
        this.name = name;
        this.type = type;
    }

    @Override
    public PrgState execute(PrgState state) throws StatementExecException, ExpressionEvalException, ADTException {
        MyIDict<String, Value> symTable = state.getSymTable();
        if(symTable.isDefined(name))
            throw new StatementExecException("Variable " + name + " is already defined");
        else
            symTable.put(name, type.defaultValue());
        state.setSymTable(symTable);
        return null;
    }

    @Override
    public MyIDict<String, Type> typecheck(MyIDict<String, Type> typeEnv) throws StatementExecException, ExpressionEvalException, ADTException {
        typeEnv.put(name, type);
        return typeEnv;
    }

    @Override
    public IStmt deepCopy() {
        return new VarDeclStmt(name, type.deepCopy());
    }

    @Override
    public String toString() {
        return type.toString() + " " + name;
    }

}
