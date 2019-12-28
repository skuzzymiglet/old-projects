import javax.swing.*;
import java.util.LinkedList;

public class ShowCards extends JFrame
{
    Deck d = new Deck();
    ImageIcon pic;
    int cardNumber = 0;
    JButton showNext = new JButton("Show Next Card");
    JPanel panel1;
    public static void main(String[] args)
    {
        new ShowCards();
    }
    public ShowCards()
    {
        panel1 = new JPanel();
        panel1.setSize(600, 800);
        pic = showCard(d.getDeck().get(cardNumber).getId());
        panel1.add(new JLabel(pic));
        panel1.add(showNext);
        show(d.getDeck().get(cardNumber).getId());
        showNext = new JButton("Show Next Card");
        showNext.addActionListener(e -> showNextCard());
    }
    private ImageIcon showCard(int id)
    {
        return new ImageIcon("/media/pi/STORE-11/Tidbits/UnoSimulator/img/cards/id" + Integer.toString(id) + ".jpg");
    }
    public void show(int id)
    {
        this.removeAll();
        this.revalidate();
        this.repaint();
        System.out.println(d.giveTop());
        //this.d.shuffle();
        this.setTitle("Show Cards");
        this.setSize(600, 800);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        panel1 = new JPanel();
        panel1.setSize(600, 800);
        pic = showCard(id);
        panel1.add(new JLabel(pic));
        panel1.add(showNext);
        this.add(panel1);
        this.pack();
        this.setVisible(true);
    }
    public void showNextCard()
    {
        if(cardNumber >= d.getDeck().size())
        {
            cardNumber = 0;
        }
        else
        {
            cardNumber++;
        }
        System.out.println("Hi");
        this.show(d.getDeck().get(cardNumber).getId());
    }
}