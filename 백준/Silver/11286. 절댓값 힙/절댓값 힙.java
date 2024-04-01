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
        
        PriorityQueue<Integer> heap = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                if (Math.abs(o1) == Math.abs(o2)) return o1-o2;
                else return Math.abs(o1)-Math.abs(o2);
            }
        });

        while(N-- > 0) {
            int x = Integer.parseInt(br.readLine());

            if(x!=0) heap.add(x);
            else if(heap.size() == 0) sb.append("0\n");
            else sb.append(heap.poll()+"\n");
        }

        System.out.print(sb.toString());
    }
}