public class TestComptes {
	
	public static void main(String[] args) {
		CompteCourant c1 = new CompteCourant();
		
		// Doit afficher un compte avec tout initialisé à 0.0 / chaine vide
		System.out.println(c1);
		
		// Affiche une ligne vide
		System.out.println();
		
		c1.setNumeroCompte(1);
		c1.setCredit(100);
		c1.setDebit(50);
		c1.setPersonne(new Personne("Neymar", "Jean"));
		c1.setDecouvertMax(1000);
		
		// Doit afficher "Nouveau compte n° : 1 appartenant a : Jean Neymar, decouvert max : 1000.0"
		System.out.println("Nouveau compte n° : " + c1.getNumeroCompte() + " appartenant a : " + c1.getPersonne() + ", decouvert max : " + c1.getDecouvertMax());
		
		System.out.println();
		
		Compte c2 = new CompteCourant(1, 1000, 500, new Personne("Morisse", "Pierre"), 100);
		// Doit afficher toutes les informations du compte correctement initialisées
		System.out.println(c2);
		
		System.out.println();
		
		c2.crediter(100);
		// Doit affichier 1100.0
		System.out.println(c2.getCredit());
		
		System.out.println();
		
		// Doit afficher 600.0
		System.out.println(c2.consulterSolde());
		
		System.out.println();
		
		c2.debiter(300);
		// Doit afficher 800.0
		System.out.println(c2.getDebit());
		
		System.out.println();
		
		// Doit afficher 300.0
		System.out.println(c2.consulterSolde());
		
		System.out.println();
		
		c2.debiter(400);
		// Doit afficher -100.0
		System.out.println(c2.consulterSolde());
		
		System.out.println();
		
		// Doit afficher un message d'erreur
		c2.debiter(1);
		
		System.out.println();
		System.out.println();
		System.out.println();
		
		CompteEpargne c3 = new CompteEpargne();
		
		// Doit afficher un compte avec tout initialisé à 0.0 / chaine vide
		System.out.println(c3);
		
		System.out.println();
		
		c3.setNumeroCompte(3);
		c3.setCredit(100);
		c3.setDebit(50);
		c3.setPersonne(new Personne("Neymar", "Jean"));
		c3.setTauxInterets(0.05);
		
		// Doit afficher "Nouveau compte n° : 3 appartenant a : Jean Neymar, taux interets : 0.05"
		System.out.println("Nouveau compte n° : " + c3.getNumeroCompte() + " appartenant a : " + c3.getPersonne() + ", taux interets : " + c3.getTauxInterets());
		
		System.out.println();
		
		// Doit afficher 2.5
		System.out.println(c3.calculerInterets());
		
		System.out.println();
		
		Compte c4 = new CompteEpargne(4, 500, 0, new Personne("Morisse", "Pierre"), 5);
		// Doit afficher toutes les informations du compte correctement initialisées
		System.out.println(c4);
		
		System.out.println();
		
		// Doit afficher un message d'erreur
		c4.debiter(501);
	}
}
