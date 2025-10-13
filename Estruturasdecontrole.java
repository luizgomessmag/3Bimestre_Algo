package estruturasdecontrole;

import java.util.Scanner;

public class Estruturasdecontrole {


    public static void main(String[] args) {
        Scanner teclado = new Scanner (System.in);
        System.out.println("Digite uma numero 1-7: ");
        int numero = teclado.nextInt();
        if (numero > 0 && numero <= 7){
            
            if (numero == 1){
                System.out.println("Segunda");

            }
            if (numero == 2){
                System.out.println("Segunda");
            }
            if (numero == 3){
                System.out.println("Terça");
            }
            if (numero == 4){
                System.out.println("Quarta");
            }
            if (numero == 5){
                System.out.println("Quinta");
            }
            if (numero == 6){
                System.out.println("Sexta");
            }
            if (numero == 7){
                System.out.println("Sábado");
            }
        }
        else{
            System.out.println("Número inválido");
        }
        
    }
}
