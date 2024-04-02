import java.io.*;
import java.util.*;

public class Main {

    static class Point {
        int x, y;

        Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] strArr;
        strArr = br.readLine().split(" ");

        int N = Integer.parseInt(strArr[0]);
        int M = Integer.parseInt(strArr[1]);

        char[][] graph = new char[N][M];
        int[] dx = {-1,0,1,0};
        int[] dy = {0,-1,0,1};
        Point start = new Point(-1,-1);
        int answer = 0;


        for(int i=0; i<N; i++) {
            graph[i] = br.readLine().toCharArray();
            for(int j=0; j<M; j++) {
                if(start.x != -1) break;
                if(graph[i][j]=='I') start = new Point(i,j);
            }
        }

        Deque<Point> q = new ArrayDeque<>();
        q.add(start);
        while(!q.isEmpty()) {
            Point cur = q.poll();
            for(int i=0; i<4; i++) {
                int nx = cur.x+dx[i];
                int ny = cur.y+dy[i];

                if(0<=nx && nx<N && 0<=ny && ny<M && graph[nx][ny]!='X') {
                    if(graph[nx][ny]=='P') answer++;
                    graph[nx][ny] = 'X';
                    q.add(new Point(nx, ny));
                }
            }
        }

        if(answer==0) System.out.println("TT");
        else System.out.println(answer);
    }
}