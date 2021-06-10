import java.util.Scanner;
public class michiApp {

     Scanner teclado = new Scanner(System.in);

    public static void main(String[] args) {
        EjercicioMishi mich=new EjercicioMishi();
        System.out.println("Bienvenido al Mishi");

        int a=0;
        while (a<=3){
            mich.imprimirmatriz();
            mich.dibujarjugador1();
            mich.imprimirmatriz();
            mich.dibujarjugador2();
            a=a+1;
        }
        mich.imprimirmatriz();
        mich.dibujarjugador1();
        mich.imprimirmatriz();



        ;
    }
}
