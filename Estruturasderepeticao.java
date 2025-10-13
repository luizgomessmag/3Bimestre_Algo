package estruturasderepeticao;

import java.util.Scanner;

public class Estruturasderepeticao {

    /* WHILE = ENQUANTO*/
    
/*    public static void main(String[] args) {
        int i = 1;
        while (i <=5){
            System.out.println(i+ " ");
            i++;
        }
        System.out.println(); 
    }*/
 
    /* WHILE = ENQUANTO*/    
    
/*      public static void main(String[] args) {
        Scanner teclado = new Scanner (System.in);
        int num = 0;
        int soma = 0;
        while (num > -1){
            System.out.println("Digite um numero (-1 para sair): ");
            num = teclado.nextInt();
            soma = soma + num; /*Ou soma += num;*/
            
/*        }
        System.out.println("Resultado: "+soma);
    }*/
    
    /* DO WHILE = REPITA*/
    
/*        public static void main(String[] args) {
            int i = 1;
            do{
                System.out.println(i+ " ");
                i++;
            }
            while (i <= 5);
            System.out.println();
        }*/
    
        public static void main(String[] args) {
            for(int i = 1; i <= 5; i++){
                System.out.println(i);
            }
            System.out.println();
        }
}
