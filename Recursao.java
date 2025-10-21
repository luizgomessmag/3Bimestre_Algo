package recursao;



public class Recursao {


    public static void main(String[] args) {
        /*contagemRepeticao(5);
        System.out.println();
        contagemRecursao(5);
        System.out.println();
        contagemP(1);
        System.out.println();
        */
        System.out.println(calculaFatorial(5));
    }

    public static void contagemRepeticao(int num1){
        for (int i = num1; i > 0; i--){
            System.out.println(i);
        }
    }
    public static void contagemRecursao(int num){
        if (num != 0){
        System.out.println(num);
        contagemRecursao(num - 1);
        }
    }
    public static void contagemP(int i){
        if (i != 0 && i <= 5){
        System.out.println(i);
        contagemP(i + 1);
        }
    }

    public static int calculaFatorial(int n){
        if (n == 1 || n == 0){
            return 1;            
        }else{
        return (n * calculaFatorial(n-1));
        }
    }
    public static void sequenciafibonacci(int n){
        /*--> FINALIZAR F(n) = F(n-1) + F(n-2)*/
                
            }

}