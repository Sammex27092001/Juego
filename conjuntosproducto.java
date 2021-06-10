import java.util.Scanner;

public class conjuntosproducto {
    Scanner teclado = new Scanner(System.in);

    public int[] ingresarA(int a) {
        int[] conjuntosa = new int[a];
        int x;
        System.out.println("El conjunto A tendra " + a + " elementos");
        int y = 1;
        for (x = 0; x < a; x++) {
            System.out.println("Ingrese el " + y + " elemento del Conjunto A");
            y = y + 1;
            conjuntosa[x] = teclado.nextInt();

        }
        int z;
        System.out.print("El conjunto A es { ");
        for (z = 0; z < a; z++) {
            int m = conjuntosa[z];
            System.out.print(m + "   ");

        }
        System.out.println("}");
        return conjuntosa;


    }

    public int[] ingresarB(int b) {
        int[] conjuntosb = new int[b];
        int x;
        System.out.println(" ");
        System.out.println("El conjunto B tendra " + b + " elementos");
        int y = 1;
        for (x = 0; x < b; x++) {
            System.out.println("Ingrese el " + y + " elemento del Conjunto B");
            y = y + 1;
            conjuntosb[x] = teclado.nextInt();

        }
        int z;
        System.out.print("El conjunto B es { ");
        for (z = 0; z < b; z++) {
            int m = conjuntosb[z];
            System.out.print(m + "   ");

        }
        System.out.println("}");
        return conjuntosb;


    }
    public void producTO(int[] cona,int[] conb,int num1,int num2){
        int a,b;
        System.out.print("Producto CARTESIANO { ");
        for(a=0;a<num1;a++){
            for (b=0;b<num2;b++){
                System.out.print("("+cona[a]+","+conb[b]+")"+";");

            }

        }
        System.out.print("}");

    }


}
