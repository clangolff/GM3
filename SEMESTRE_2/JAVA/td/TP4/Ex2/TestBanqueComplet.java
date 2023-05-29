import java.util.ArrayList;
import java.util.Set;
import java.util.Iterator;

public class TestBanqueComplet {
	
	public static void main(String[] args) {
        Personne p1 = new Personne("Morisse", "Pierre", new ArrayList<Compte>());
        Personne p2 = new Personne("Neymar", "Jean", new ArrayList<Compte>());

		CompteCourant c1 = new CompteCourant(1, 500, 0, p1, 500);
		CompteEpargne c2 = new CompteEpargne(2, 1000, 0, p1, 0.10);
		
		CompteCourant c3 = new CompteCourant(3, 1000, 300, p2, 5);
		CompteEpargne c4 = new CompteEpargne(4, 1000, 100, p2, 0.05);
		
		// Doit affichier "Pierre Morisse possede : 0 compte(s)"
		System.out.println(p1 + " possede : " + p1.getComptes().size() + " compte(s)");
		// Doit afficher "Jean Neymar possede : 0 compte(s)"
		System.out.println(p2 + " possede : " + p2.getComptes().size() + " compte(s)");
		
		System.out.println();
		
		BanqueInt b = new Banque("Credit Agricole", "Rouen");
		b.ajouterCompte(c1);
		b.ajouterCompte(c3);
		
		// Doit affichier "Pierre Morisse possede : 1 compte(s)"
		System.out.println(p1 + " possede : " + p1.getComptes().size() + " compte(s)");
		// Doit afficher "Jean Neymar possede : 1 compte(s)"
		System.out.println(p2 + " possede : " + p2.getComptes().size() + " compte(s)");
		
		System.out.println();
		
		p1.ajouterCompte(c2);
		p2.ajouterCompte(c4);
		
		// Doit affichier "Pierre Morisse possede : 2 compte(s)"
		System.out.println(p1 + " possede : " + p1.getComptes().size() + " compte(s)");
		// Doit afficher "Jean Neymar possede : 2 compte(s)"
		System.out.println(p2 + " possede : " + p2.getComptes().size() + " compte(s)");
		
		System.out.println();
		
		b.ajouterCompte(c2);
		b.ajouterCompte(c4);
		
		// Doit affichier "Pierre Morisse possede : 2 compte(s)"
		System.out.println(p1 + " possede : " + p1.getComptes().size() + " compte(s)");
		// Doit afficher "Jean Neymar possede : 2 compte(s)"
		System.out.println(p2 + " possede : " + p2.getComptes().size() + " compte(s)");
		
		System.out.println();
		
		System.out.println(p1.getComptes().get(0));
		
		System.out.println();
		
		// On interdit les découverts pour tous les comptes courants
		Set<CompteCourant> comptesCourants = b.getComptesCourants();
		Iterator<CompteCourant> it = comptesCourants.iterator();
		while (it.hasNext()) {
			CompteCourant c = it.next();
			c.setDecouvertMax(0);
		}
		
		// Doit afficher un message d'erreur, car le premier compte de p1 a 500 de credit, et 0 de decouvert max
		p1.getComptes().get(0).debiter(501);
		
		System.out.println();
		
		b.supprimerCompte(c2);
		b.supprimerCompte(c4);
		
		// Doit affichier "Pierre Morisse possede : 1 compte(s)"
		System.out.println(p1 + " possede : " + p1.getComptes().size() + " compte(s)");
		// Doit afficher "Jean Neymar possede : 1 compte(s)"
		System.out.println(p2 + " possede : " + p2.getComptes().size() + " compte(s)");
		// Doit afficher 2
		System.out.println(b.nombreDeComptes());
		
		System.out.println();
		
		p1.supprimerCompte(c1);
		p2.supprimerCompte(c3);
		
		// Doit affichier "Pierre Morisse possede : 0 compte(s)"
		System.out.println(p1 + " possede : " + p1.getComptes().size() + " compte(s)");
		// Doit afficher "Jean Neymar possede : 0 compte(s)"
		System.out.println(p2 + " possede : " + p2.getComptes().size() + " compte(s)");
		// Doit afficher 2 : supprimer un compte a partir d'une Personne ne le retire pas de la Banque
		System.out.println(b.nombreDeComptes());
	}
}
