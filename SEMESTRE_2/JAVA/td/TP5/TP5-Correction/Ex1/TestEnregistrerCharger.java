import java.util.ArrayList;
import java.util.Set;
import java.util.Iterator;

public class TestEnregistrerCharger {
	
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
		
		b.enregistrer("premiereSauvegarde.txt");
		
		BanqueInt b1 = new Banque();
		b1.charger("premiereSauvegarde.txt");
		
		System.out.println(b1);
		
		b1.enregistrer("deuxiemeSauvegarde.txt");
	}
}
