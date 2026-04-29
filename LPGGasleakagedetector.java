import java.util.Scanner;

public class LPGGasLeakageDetector {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int gasLevel;

        System.out.println("===== LPG Gas Leakage Detector =====");

        System.out.print("Enter Gas Sensor Value: ");
        gasLevel = sc.nextInt();

        if (gasLevel > 300) {
            System.out.println("\nGas Leakage Detected!");
            System.out.println("Alarm ON");
            System.out.println("Regulator OFF");
            System.out.println("Open Windows Immediately");
        } else {
            System.out.println("\nGas Level Normal");
            System.out.println("System Safe");
        }

        sc.close();
    }
}