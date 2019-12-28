import java.util.*;

public class Lookup
{
    static Scanner sc = new Scanner(System.in);
    static Card toSearch;
    public static void main(String[] args)
    {
        System.out.println("'q' to quit");
        while(true)
        {
            System.out.print("Enter card id: ");
            try
            {
                int x = sc.nextInt();
                toSearch = new Card(x);
            }
            catch (Exception e)
            {
                String x = sc.nextLine();
                if(x.toLowerCase().equals("q"))
                {
                    System.exit(0);
                }
                else
                {
                    continue;
                }
            }
            try
            {
                System.out.print(toSearch.getColor());
                System.out.println(toSearch.getType());
            }
            catch (ArrayIndexOutOfBoundsException e)
            {
                System.out.println("That does not exist");
            }
        }
   }
}
