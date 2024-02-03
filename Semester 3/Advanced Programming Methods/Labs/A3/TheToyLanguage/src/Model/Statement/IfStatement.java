package Model.Statement;

import Collection.Stack.MyIStack;
import Exception.StatementExecutionException;
import Exception.ToyLanguageInterpreterException;
import Model.Expression.IExpression;
import Model.State.ProgramState;
import Model.Value.BooleanValue;
import Model.Value.Value;

public class IfStatement implements IStatement {
    IExpression expression;
    IStatement thenStatement;
    IStatement elseStatement;

    public IfStatement(IExpression expression, IStatement thenStatement, IStatement elseStatement){

        this.expression=expression;
        this.thenStatement=thenStatement;
        this.elseStatement=elseStatement;
    }

    @Override
    public ProgramState execute(ProgramState state) throws ToyLanguageInterpreterException {
        Value result = this.expression.evaluate(state.getSymbolTable());

        if (result instanceof BooleanValue boolResult) {
            IStatement statement;

            if (boolResult.getValue()) {
                statement = this.thenStatement;
            } else {
                statement = this.elseStatement;
            }

            MyIStack<IStatement> stack = state.getExecutionStack();
            stack.push(statement);
            state.setExecutionStack(stack);
            return state;
        }
        else{
            throw new StatementExecutionException("Please provide a boolean expression in an if statement.");
        }
    }

    @Override
    public String toString(){
        return String.format("if(%s){%s}else{%s}", this.expression.toString(), this.thenStatement.toString(), this.elseStatement.toString());    }
}
