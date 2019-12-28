import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.io.IOException;

public class Test
{
    public static void main(String[] args)
    {
        Dog myPet = new Dog("Fido", "Labrador", Gender.MALE, true, "99 Kings Road");
        try
        {
            FileOutputStream fos = new FileOutputStream("myPet.ser");
            ObjectOutputStream oos = new ObjectOutputStream(fos);
            oos.writeObject(myPet);
            oos.close();
            fos.close();
            System.out.println("Serialzation Done!!");
        }
        catch(IOException ioe)
        {
            System.out.println(ioe);
        }
    }
}
