import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int count_five = 0;
        
        for(int i=n; i>0; i--)
            for(int j=i; j%5==0; count_five++, j/=5);

        System.out.println(count_five);
    }
}