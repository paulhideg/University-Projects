package model.statements;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import exceptions.StatementExecException;
import model.expressions.IExpression;
import model.programState.PrgState;
import model.type.BooleanType;
import model.type.Type;
import model.utils.MyIDict;
import model.utils.MyIStack;
import model.value.BooleanValue;
import model.value.Value;

public class WhileStmt implements IStmt{

    private final IExpression exp;
    private final IStmt stmt;

    public WhileStmt(IExpression exp, IStmt stmt){

        this.exp = exp;
        this.stmt =  stmt;
    }

    @Override
    public PrgState execute(PrgState state) throws StatementExecException, ExpressionEvalException, ADTException{

        Value value = exp.eval(state.getSymTable(), state.getHeap());

        if(!(value instanceof BooleanValue))
            throw new StatementExecException("While statement: expression is not a boolean");

        MyIStack<IStmt> exeStack = state.getExeStack();

        BooleanValue boolValue = (BooleanValue) value;

        if(boolValue.getValue()) {
            exeStack.push(this);
            exeStack.push(stmt);
        }
        state.setExeStack(exeStack);
        return null;
    }

    @Override
    public MyIDict<String, Type> typecheck(MyIDict<String, Type> typeEnv) throws StatementExecException, ExpressionEvalException, ADTException {

        Type typeExp = exp.typecheck(typeEnv);
        if (typeExp.equals(new BooleanType())) {
            stmt.typecheck(typeEnv.deepCopy());
            return typeEnv;
        } else {
            throw new StatementExecException("The condition of WHILE has not the type bool");
        }
    }

    @Override
    public IStmt deepCopy() {
        return new WhileStmt(exp.deepCopy(), stmt.deepCopy());
    }

    @Override
    public String toString(){
        return "while(" + exp.toString() + ") " + stmt.toString();
    }

}
