import java.io.*;
import java.util.ArrayList;

public class GameConfiguration
{
    File file;
    FileInputStream fis;
    BufferedInputStream bis;
    public GameConfiguration(String file)
    {
        this.file = new File(file);
        try
        {
            this.fis = new FileInputStream(this.file);
            this.bis = new BufferedInputStream(fis);
            for(String line : lines(bis))
            {
                for(String side: line.split(":"))
                {
                    System.out.print(side);
                }
                System.out.println();
            }
        }
        catch(IOException ioe)
        {
            System.out.println("IOException: " + ioe);
        }
    }
    public String[] lines(BufferedInputStream bis)
    {
        String text = "";
        try
        {
            while(bis.available() > 0)
            {
                text += (char)bis.read();
            }
            return text.split("\n");
        }
        catch(Exception e)
        {
            return null;
        }
    }
    public String[][] properties(String[] lines)
    {
        int numOfLines = lines.length;
        String[][] props = new String[numOfLines][2];
        String[] splitted;
        for(int line=0; line >= numOfLines; line++)
        {
            splitted = lines[line].split(":");
            props[line][0] = splitted[0];
            props[line][1] = splitted[1];
        }
        return props;
    }
}
