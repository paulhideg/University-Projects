package model.statements;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import exceptions.StatementExecException;
import model.programState.PrgState;
import model.type.BooleanType;
import model.type.Type;
import model.utils.MyIDict;
import model.utils.MyIStack;
import model.expressions.IExpression;
import model.value.BooleanValue;
import model.value.Value;

public class IfStmt implements IStmt{
    IExpression exp;
    IStmt thenStmt;
    IStmt elseStmt;

    public IfStmt(IExpression exp, IStmt thenStmt, IStmt elseStmt) {
        this.exp = exp;
        this.thenStmt = thenStmt;
        this.elseStmt = elseStmt;
    }

    @Override
    public MyIDict<String, Type> typecheck(MyIDict<String, Type> typeEnv) throws StatementExecException, ExpressionEvalException, ADTException {
        Type typeExp = exp.typecheck(typeEnv);
        if (typeExp.equals(new BooleanType())) {
            thenStmt.typecheck(typeEnv.deepCopy());
            elseStmt.typecheck(typeEnv.deepCopy());
            return typeEnv;
        } else {
            throw new StatementExecException("The condition of IF has not the type bool");
        }
    }

    @Override
    public PrgState execute(PrgState state) throws StatementExecException, ExpressionEvalException, ADTException {
        Value val = exp.eval(state.getSymTable(), state.getHeap());
        if (val instanceof BooleanValue) {
            BooleanValue boolVal = (BooleanValue) val;
            MyIStack<IStmt> exeStack = state.getExeStack();
            if (boolVal.getValue())
                exeStack.push(thenStmt);
            else
                exeStack.push(elseStmt);
            state.setExeStack(exeStack);
            return null;
        } else
            throw new StatementExecException("If statement: expression is not a boolean");
    }

    @Override
    public IStmt deepCopy() {
        return new IfStmt(exp.deepCopy(), thenStmt.deepCopy(), elseStmt.deepCopy());
    }

    @Override
    public String toString() {
        return "IF(" + exp.toString() + ") THEN(" + thenStmt.toString() + ") ELSE(" + elseStmt.toString() + ")";
    }

}
