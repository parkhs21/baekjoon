import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int arr[] = new int[n+1];
        arr[1] = 1;

        for(int i=2; i<=n; i++) {
            arr[i] = arr[i-1]+1;
            for(int j=(int) Math.sqrt(i); j>1; j--) {
                if(i == j*j) {
                    arr[i] = 1;
                    break;
                }
                arr[i] = Math.min(arr[i], arr[i - j*j] + 1);
            }
        }


        System.out.print(arr[n]);
    }
}