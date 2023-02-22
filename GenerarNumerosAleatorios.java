package clase1;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class GenerarNumerosAleatorios {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Por favor, proporcione el nombre del archivo de salida como argumento");
            System.exit(1);
        }

        int cantidadNumeros = 1000000;
        int minValor = -10000000;
        int maxValor = 10000000;

        Random rand = new Random();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < cantidadNumeros; i++) {
            int numeroAleatorio = rand.nextInt(maxValor - minValor + 1) + minValor;
            sb.append(numeroAleatorio);
            sb.append("\n");
        }

        String nombreArchivo = args[0];
        try {
            FileWriter writer = new FileWriter(nombreArchivo);
            writer.write(sb.toString());
            writer.close();
            System.out.println("Se han generado " + cantidadNumeros + " números aleatorios y se han almacenado en el archivo " + nombreArchivo);
        } catch (IOException e) {
            System.out.println("Ha ocurrido un error al escribir en el archivo " + nombreArchivo);
            e.printStackTrace();
        }
    }
}
