public class Dog implements java.io.Serializable
{
    private String breed;
    private Gender gender;
    private String name;
    private boolean malts;
    private String vetAdress;
    public Dog(String name, String breed, Gender gender, boolean malts, String vetAdress)
    {
        this.breed = breed;
        this.gender = gender;
        this.name = name;
        this.malts = malts;
        this.vetAdress = vetAdress;
    }
}
