import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n, count = 0;
        Scanner s = new Scanner(System.in);

        n = Integer.parseInt(s.next()); // 거슬러 줘야할 금액 입력받기
        int[] Coin = new int[]{500, 100, 50, 10};

        for (int i = 0; i < 4; i++) {
            count += n / Coin[i];
            n %= Coin[i];
        }
        System.out.println(count);
    }
}
