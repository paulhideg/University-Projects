package model.statements;

import exceptions.ADTException;
import exceptions.ExpressionEvalException;
import exceptions.StatementExecException;
import model.expressions.IExpression;
import model.programState.PrgState;
import model.type.StringType;
import model.type.Type;
import model.utils.MyIDict;
import model.value.StringValue;
import model.value.Value;

import java.io.BufferedReader;
import java.io.IOException;

public class CloseReadFileStmt implements IStmt {

    private final IExpression expression;

    public CloseReadFileStmt(IExpression expression) {
        this.expression = expression;
    }

    @Override
    public  MyIDict<String, Type> typecheck(MyIDict<String, Type> typeEnv) throws StatementExecException, ExpressionEvalException, ADTException {
        Type type = expression.typecheck(typeEnv);
        if (type.equals(new StringType())) {
            return typeEnv;
        } else {
            throw new StatementExecException("CloseReadFileStmt: expression is not a string");
        }
    }


    @Override
    public PrgState execute(PrgState state) throws StatementExecException, ExpressionEvalException, ADTException {
        Value value = expression.eval(state.getSymTable(), state.getHeap());
        if (!value.getType().equals(new StringType()))
            throw new StatementExecException(String.format("%s does not evaluate to StringValue", expression));
        StringValue fileName = (StringValue) value;
        MyIDict<String, BufferedReader> fileTable = state.getFileTable();
        if (!fileTable.isDefined(fileName.getValue()))
            throw new StatementExecException(String.format("%s is not present in the FileTable", value));
        BufferedReader br = fileTable.lookup(fileName.getValue());
        try {
            br.close();
        } catch (IOException e) {
            throw new StatementExecException(String.format("Unexpected error in closing %s", value));
        }
        fileTable.remove(fileName.getValue());
        state.setFileTable(fileTable);
        return null;
    }

    public IStmt deepCopy() {
        return new CloseReadFileStmt(expression.deepCopy());
    }
    @Override
    public String toString() {
        return String.format("closeReadFile(%s)", expression.toString());
    }
}

