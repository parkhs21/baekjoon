import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static long arr[] = new long[101];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        arr[1] = arr[2] = arr[3] = 1L;
        arr[4] = arr[5] = 2L;

        int T = Integer.parseInt(br.readLine());
        while(T-- > 0) {
            int N = Integer.parseInt(br.readLine());
            sb.append(padovan(N)+"\n");
        }

        System.out.print(sb.toString());
    }

    public static long padovan(int N) {
        if(arr[N]==0) arr[N] = padovan(N-1)+padovan(N-5);
        return arr[N];
    }
}