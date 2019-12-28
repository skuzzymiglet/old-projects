import javax.swing.*;

public class LookupGUI extends JFrame
{
    public static void main(String[] args)
    {
        new LookupGUI();
    }
    public LookupGUI()
    {
        this.setSize(800, 200);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setTitle("Enter Card ID - Lookup GUI");
        
        JPanel panel1 = new JPanel();
        
        JButton[] buttons = new JButton[54];
        
        for(int i = 0; i <= 53; i++)
        {
            buttons[i] = new JButton(Integer.toString(i));
        }
        for(JButton x : buttons)
        {
           panel1.add(x);
        }
        this.add(panel1);
        
        this.setVisible(true);
    }
}