import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        int n, k, count = 0;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        while (n > 1) {
            if (n < k) {
                count += n - 1;
                n = 1;
            }
            else {
                if (n % k == 0) {
                    n /= k;
                }
                else {
                    n -= 1;
                }
                count++;
            }
        }
        System.out.println(count);
    }
}
