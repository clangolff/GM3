import java.util.ArrayList;
import java.util.Set;
import java.util.Iterator;
import java.io.FileOutputStream;
import java.io.FileInputStream;
import java.io.ObjectOutputStream;
import java.io.ObjectInputStream;
import java.io.File;

public class TestSerialisation {
	
	public static void main(String[] args) {
        Personne p1 = new Personne("Morisse", "Pierre", new ArrayList<Compte>());
        Personne p2 = new Personne("Neymar", "Jean", new ArrayList<Compte>());

		CompteCourant c1 = new CompteCourant(1, 500, 0, p1, 500);
		CompteEpargne c2 = new CompteEpargne(2, 1000, 0, p1, 0.10);
		
		CompteCourant c3 = new CompteCourant(3, 1000, 300, p2, 5);
		CompteEpargne c4 = new CompteEpargne(4, 1000, 100, p2, 0.05);
		
		BanqueInt b = new Banque("Credit Agricole", "Rouen");
		b.ajouterCompte(c1);
		b.ajouterCompte(c2);
		b.ajouterCompte(c3);
		b.ajouterCompte(c4);
		
		System.out.println(b);
		
		try {
			File fichier =  new File("troisiemeSauvegarde") ;
            // Enregistrement de l'état de la banque dans le fichier troisiemeSauvegarde
			FileOutputStream fos = new FileOutputStream(fichier);
			ObjectOutputStream oos = new ObjectOutputStream(fos);
			oos.writeObject(b);
			
			fichier =  new File("troisiemeSauvegarde");
            BanqueInt b1;
            // Chargement de la banque b1 à partie du fichier troisiemeSauvegarde			
            
			
			System.out.println(b1);
			
			System.out.println("Comptes courants de b : ");
			for (CompteCourant c : b.getComptesCourants()) {
				System.out.println(c);
			}
			
			System.out.println("Comptes courants de b1 : ");
			for (CompteCourant c : b1.getComptesCourants()) {
				System.out.println(c);
			}
			
			System.out.println();
			
			System.out.println("Comptes epagne de b : ");
			for (CompteEpargne c : b.getComptesEpargne()) {
				System.out.println(c);
			}
			
			System.out.println("Comptes epargne de b1 : ");
			for (CompteEpargne c : b1.getComptesEpargne()) {
				System.out.println(c);
			}
			
			
		} catch (Exception e) {
			System.out.println("Exception : " + e);
		}
	}
}
