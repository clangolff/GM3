public class TestBanque {
	
	public static void main(String[] args) {		
		CompteCourant c1 = new CompteCourant(1, 1000, 500, new Personne("Morisse", "Pierre"), 100);
		CompteCourant c2 = new CompteCourant(2, 1000, 300, new Personne("Neymar", "Jean"), 500);
		
		CompteEpargne c3 = new CompteEpargne(3, 1000, 500, new Personne("Morisse", "Pierre"), 0.05);
		CompteEpargne c4 = new CompteEpargne(3, 1000, 500, new Personne("Morisse", "Pierre"), 0.05);
		
		BanqueInt b = new Banque("Credit Agricole", "Rouen");
		b.ajouterCompte(c1);
		b.ajouterCompte(c3);
		b.ajouterCompte(c4);
		
		// Doit afficher true
		System.out.println("b.estPresent(c1) : " + (b.estPresent(c1)));
		// Doit afficher false
		System.out.println("b.estPresent(c2) : " + (b.estPresent(c2)));
		// Doit afficher true
		System.out.println("b.estPresent(c3) : " + (b.estPresent(c3)));
		// Doit afficher true
		System.out.println("b.estPresent(c4) : " + (b.estPresent(c4)));
		
		System.out.println();
		
		b.ajouterCompte(c2);
		// Doit afficher true
		System.out.println("b.estPresent(c2) : " + (b.estPresent(c2)));
		
		System.out.println();
		
		CompteCourant c5 = new CompteCourant(5, 1000, 500, new Personne("Pelle", "Sarah"), 800);
		b.ajouterCompte(c5);
		b.supprimerCompte(c5);
		
		// Doit afficher 3
		System.out.println(b.nombreDeComptes());
	}
}
