import java.util.Scanner;
public class Hexadecimal {
    Scanner teclado = new Scanner(System.in);

        String a=recepcionar();
        String [] array = new String[a.length()];

    public String recepcionar() {
        System.out.println ("Recuerde que solo permite números y A,B,C,D,E,F ");
        System.out.print("Inserte el numéro en base 16 : ");

        String num2 = teclado.nextLine();
        return num2;
    }
   public void Guardarenarray(){


        for (int b=0;b<a.length();b++){
            array[b]= String.valueOf(a.charAt(b));

        }

   }
   public void Verificar(){
       for (int b=0;b<a.length();b++){
           if(array[b]!= "0" ||  array[b]!= "1" || array[b]!= "2" ||array[b]!= "3" ||array[b]!= "4" ||array[b]!= "5" ||
                   array[b]!= "6" ||array[b]!= "7" ||array[b]!= "8" ||array[b]!= "9" ||array[b]!= "A" ||array[b]!= "B" ||
                   array[b]!= "C" ||array[b]!= "D" ||array[b]!= "E" || array[b]!= "F" )
           {
               System.out.print("Número Incorrecto");
               System.exit(0);
           }


       }
   }
   public void Imprimirarray(){
       System.out.print("El número hexadecimal es :");
       for (int b=0;b<a.length();b++){
           System.out.print(array[b]);

       }
       System.out.println("  ");
   }
    public static int caracterHexadecimalADecimal(char caracter) {
        switch (caracter) {
            case 'A':
                return 10;
            case 'B':
                return 11;
            case 'C':
                return 12;
            case 'D':
                return 13;
            case 'E':
                return 14;
            case 'F':
                return 15;
            default:
                return Integer.parseInt(String.valueOf(caracter));
        }
    }

    public  int  hexadecimalADecimal() {
        int  decimal = 0;
        // Saber en cuál posición de la cadena (de izquierda a derecha) vamos
        int potencia = 0;
        // Recorrer la cadena de derecha a izquierda
        for (int x = a.length() - 1; x >= 0; x--) {
            int valor = caracterHexadecimalADecimal(a.charAt(x));
            long elevado = (long) Math.pow(16, potencia) * valor;
            decimal += elevado;
            // Avanzar en la potencia
            potencia++;
        }
        System.out.println("El número en base 10 es : "+ decimal);
        return decimal;
    }

    public  String decimalAOctal(int decimal) {
        int residuo;
        String octal = "";
        char[] caracteresOctales = {'0', '1', '2', '3', '4', '5', '6', '7'};
        while (decimal > 0) {
            residuo = decimal % 8;
            char caracter = caracteresOctales[residuo];
            octal = caracter + octal;
            decimal = decimal / 8;
        }
        System.out.println("El número en base 8 es: "+octal);
        return octal;
    }

}
