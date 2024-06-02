package entidades;

import java.util.Scanner;

public class PorHora extends Funcionario{
    private double taxaHoraria;
    private double horas;

    public PorHora(){
        super();
    }
    
    public PorHora(String nome, double taxaHoraria, double horas) {
        super(nome);
        this.taxaHoraria = taxaHoraria;
        this.horas = horas;
    }

    public double getTaxaHoraria() {
        return taxaHoraria;
    }

    public void setTaxaHoraria(double taxaHoraria) {
        this.taxaHoraria = taxaHoraria;
    }

    public double getHoras() {
        return horas;
    }

    public void addHoras(double horas) {
        this.horas += horas;
    }

    public double receber() {
        return taxaHoraria * horas;
    }

    public void inserirDados() {
        Scanner sc = new Scanner(System.in);

        System.out.println("Informe o nome do funcionario horista: ");
        String nome = sc.nextLine();

        System.out.println("Informe a taxa horario: ");
        double taxa = sc.nextDouble();

        System.out.println("Informe a quantidades de horas: ");
        double horas = sc.nextDouble();

        this.nome = nome;
        this.taxaHoraria = taxa;
        this.horas = horas;
    }

}
