package UserInterface;

import Controller.Controller;
import Model.Expression.ArithmeticExpression;
import Model.Expression.RelationalExpression;
import Model.Expression.ValueExpression;
import Model.Expression.VariableExpression;
import Model.State.ProgramState;
import Model.Statement.*;
import Model.Type.BooleanType;
import Model.Type.IntType;
import Model.Value.BooleanValue;
import Model.Value.IntValue;
import Model.Type.StringType;
import Model.Value.StringValue;
import Repository.IRepository;
import Repository.Repository;

public class Interpreter {
    public static void main(String[] args) {

        IStatement ex1 = new CompoundStatement(new VariableDeclarationStatement("v",new IntType()),
                new CompoundStatement(new AssignStatement("v",new ValueExpression(new IntValue(2))),
                        new PrintStatement(new VariableExpression("v"))));

        ProgramState prg1 = new ProgramState(ex1);
        IRepository repo1 = new Repository("1.txt");
        Controller serv1 = new Controller(repo1);
        serv1.addProgram(prg1);


        IStatement ex2 = new CompoundStatement(new VariableDeclarationStatement("a", new IntType()),
                new CompoundStatement(new VariableDeclarationStatement("b", new IntType()),
                        new CompoundStatement(new AssignStatement("a", new ArithmeticExpression('+', new ValueExpression(new IntValue(2)),
                                new ArithmeticExpression('*', new ValueExpression(new IntValue(3)), new ValueExpression(new IntValue(5))))),
                                new CompoundStatement(new AssignStatement("b", new ArithmeticExpression('+', new VariableExpression("a"),
                                        new ValueExpression(new IntValue(1)))), new PrintStatement(new VariableExpression("b"))))));

        ProgramState prg2 = new ProgramState(ex2);
        IRepository repo2 = new Repository("2.txt");
        Controller serv2 = new Controller(repo2);
        serv2.addProgram(prg2);

        IStatement ex3 = new CompoundStatement(new VariableDeclarationStatement("a", new BooleanType()),
                new CompoundStatement(new VariableDeclarationStatement("v", new IntType()),
                        new CompoundStatement(new AssignStatement("a", new ValueExpression(new BooleanValue(true))),
                                new CompoundStatement(new IfStatement(new RelationalExpression(new ValueExpression(new IntValue(4)), (new ValueExpression(new IntValue(5))), "<"),
                                        new AssignStatement("v", new ValueExpression(
                                        new IntValue(2))), new AssignStatement("v", new ValueExpression(new IntValue(3)))),
                                        new PrintStatement(new VariableExpression("v"))))));

        ProgramState prg3 = new ProgramState(ex3);
        IRepository repo3 = new Repository("3.txt");
        Controller serv3 = new Controller(repo3);
        serv3.addProgram(prg3);

        IStatement ex4 = new CompoundStatement(new VariableDeclarationStatement("varf",new StringType()),new CompoundStatement(
                new AssignStatement("varf",new ValueExpression(new StringValue("test.in"))),new CompoundStatement(
                    new OpenFileStatement(new VariableExpression("varf")),new CompoundStatement(
                        new VariableDeclarationStatement("varc",new IntType()),new CompoundStatement(
                            new ReadFileStatement(new VariableExpression("varf"),"varc"),new CompoundStatement(
                                new PrintStatement(new VariableExpression("varc")),new CompoundStatement(
                                    new ReadFileStatement(new VariableExpression("varf"),"varc") ,
                                        new CompoundStatement(new PrintStatement(new VariableExpression("varc")),
                                                new CloseFileStatement(new VariableExpression("varf"))))))))));

        ProgramState prg4 = new ProgramState(ex4);
        IRepository repo4 = new Repository("4.txt");
        Controller serv4 = new Controller(repo4);
        serv4.addProgram(prg4);

        TextMenu menu = new TextMenu();
        menu.addCommand(new ExitCommand("0", "exit"));
        menu.addCommand(new RunExample("1", ex1.toString(), serv1));
        menu.addCommand(new RunExample("2", ex2.toString(), serv2));
        menu.addCommand(new RunExample("3", ex3.toString(), serv3));
        menu.addCommand(new RunExample("4", ex4.toString(), serv4));
        menu.show();
    }
}
