
/*Luiz Henrique Gomes*/

package modularizacao;

import java.util.Scanner;

public class Modularizacao {

/* -> Ajuda a responder a QUESTÃO 01 dos exercícios
    
    
    public static void main(String[] args) {
        Scanner teclado = new Scanner (System.in);
        System.out.println("Digite o nome: ");
        String nome = teclado.nextLine();
        exibirSaudacao(nome);
    }
    
    public static void exibirSaudacao(String nome){
        System.out.println("Olá " +nome+ ", bem-vindo!");
    }
*/
    
    public static void main(String[] args) {
        Scanner teclado = new Scanner (System.in);
        System.out.println("Digite o nome: ");
        String nome = teclado.nextLine();
        
        /*System.out.println(calcularMedia(10, 8)); -> calcula a media com os valores fornecidos*/
        System.out.println("Digite o n1: ");
        double n1 = teclado.nextDouble();
        System.out.println("Digite o n2: ");
        double n2 = teclado.nextDouble();
        exibirSaudacao(nome, n1, n2);
        
        
    }
    

    
    public static double calcularMedia(double n1, double n2){
        double media = (n1 + n2)/2;
        return media;
    }
    
        public static void exibirSaudacao(String nome, Double n1, Double n2){
        System.out.println("Olá " +nome+ ", bem-vindo!");
        System.out.println("Média: " +calcularMedia(n1, n2));
        System.out.println(verificaMedia(calcularMedia(n1, n2)));
    }

    public static boolean verificaMedia(double media){
        if(media >= 6){
            System.out.println("Aprovado, sua média é: " +media);
            return true;
        }
        else{
            System.out.println("Reprovado, sua média é: " +media);
            return false; 
       }
    }
}