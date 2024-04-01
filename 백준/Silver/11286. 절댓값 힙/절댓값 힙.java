import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        
        PriorityQueue<int[]> heap = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if(o1[0] < o2[0]) return -1;
                else if(o1[0] > o2[0]) return 1;
                else if(o1[1] < o2[1]) return -1;
                else if(o1[1] > o2[1]) return 1;
                return 0;
            }
        });

        while(N-- > 0) {
            int x = Integer.parseInt(br.readLine());

            if(x!=0) heap.add(new int[] {Math.abs(x), x});
            else if(heap.size() == 0) sb.append("0\n");
            else sb.append(heap.poll()[1]+"\n");
        }

        System.out.print(sb.toString());
    }
}