package entidades;

import java.util.Scanner;

public class Assalariado extends Funcionario{
    private double salario;

    public Assalariado() {
        super();
    }

    public Assalariado(String nome, double salario) {
        super(nome);
        this.salario = salario;
    }

    public double getSalario() {
        return salario;
    }

    public void setSalario(double salario) {
        this.salario = salario;
    }

    public double receber() {
        return salario; 
    }

    public void inserirDados() {
        Scanner sc = new Scanner(System.in);

        System.out.println("Informe o nome do funcionario assalariado: ");
        String nome = sc.nextLine();

        System.out.println("Informe o salario: ");
        double salario = sc.nextDouble();

        this.nome = nome;
        this.salario = salario;
    }
}
