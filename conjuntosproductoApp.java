import java.util.Scanner;
public class conjuntosproductoApp {
    public static void main(String[] args) {
        Scanner teclado=new Scanner(System.in);
        System.out.print("Ingrese cuantos elementos tendra el conjunto A : ");
        int a=teclado.nextInt();
        System.out.print("Ingrese cuantos elementos tendra el conjunto B : ");
        int b=teclado.nextInt();
        conjuntosproducto conjun=new conjuntosproducto();
        int[] cona=conjun.ingresarA(a);
        int[] conb=conjun.ingresarB(b);
        conjun.producTO(cona,conb,a,b);


    }
}