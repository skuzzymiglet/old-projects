import javax.swing.*;
import java.util.Scanner;

public class ShowCards2 extends JFrame
{
    Deck d = new Deck();
    {
        d.shuffle();
        d.addToPlayDeck(4);
    }
    Player p = new Player(d, "Muhammad");
    ImageIcon pic;
    int cardNumber = 0;
    JPanel panel1;
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args)
    {
        ShowCards2 s = new ShowCards2();
        if(sc.nextLine().equals("Hi"))
        {
            s = new ShowCards2();
        }
    }
    public ShowCards2()
    {
            System.out.println(d.giveTop());
            //this.d.shuffle();
            this.setTitle("Show Cards");
            this.setSize(600, 800);
            this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            panel1 = new JPanel();
            panel1.setSize(600, 800);
            for(Card c : p.getCards())
            {
                pic = new ImageIcon("/media/pi/STORE-11/Tidbits/UnoSim/img/cards/id" + Integer.toString(c.getId()) + ".jpg");
                panel1.add(new JLabel(pic));
            }
            this.add(panel1);
            this.pack();
            this.setVisible(true);
    }
}