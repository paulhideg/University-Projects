package model.statements;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import exceptions.StatementExecException;
import model.programState.PrgState;
import model.type.Type;
import model.utils.MyDict;
import model.utils.MyIDict;
import model.utils.MyIStack;
import model.utils.MyStack;
import model.value.Value;

import java.util.Map;

public class ForkStmt implements IStmt{
    private final IStmt statement;

    public ForkStmt(IStmt statement){
        this.statement = statement;
    }

    @Override
    public MyIDict<String, Type> typecheck(MyIDict<String, Type> typeEnv) throws StatementExecException, ExpressionEvalException, ADTException {
        return statement.typecheck(typeEnv);
    }

    @Override
    public PrgState execute(PrgState state) throws StatementExecException, ExpressionEvalException, ADTException {
        MyIStack<IStmt> newStack = new MyStack<>();
        newStack.push(statement);
        MyIDict<String, Value> newSymTable = new MyDict<>();
        for(Map.Entry<String,Value> entry : state.getSymTable().getContent().entrySet()){
            newSymTable.put(entry.getKey(), entry.getValue().deepCopy());
        }

        return new PrgState(newStack, newSymTable, state.getOut(), state.getFileTable(), state.getHeap());
    }

    @Override
    public IStmt deepCopy(){
        return new ForkStmt(statement.deepCopy());
    }

    @Override
    public String toString() {
        return "fork(" + statement.toString() + ")";
    }
}
