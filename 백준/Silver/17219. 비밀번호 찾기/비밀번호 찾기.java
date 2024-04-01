import java.io.IOException;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashMap<String, String> hash = new HashMap<String, String>(N);

        for(int i=0; i<N; i++) {
            st = new StringTokenizer(br.readLine());
            hash.put(st.nextToken(), st.nextToken());
        }

        for(int i=0; i<M; i++) {
            st = new StringTokenizer(br.readLine());
            bw.write(hash.get(st.nextToken())+"\n");
        }

        bw.close();
    }
}