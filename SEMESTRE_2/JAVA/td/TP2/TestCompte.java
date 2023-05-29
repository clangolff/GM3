public class TestCompte {
	
	public static void main(String[] args) {
		Compte c1 = new CompteBancaire();
		
		// Doit afficher un compte avec tout initialisé à 0.0 / chaine vide
		System.out.println(c1);
		
		// Affiche une ligne vide
		System.out.println();
		
		c1.setNumeroCompte(1);
		c1.setCredit(100);
		c1.setDebit(50);
		c1.setPersonne(new Personne("Neymar", "Jean"));
		
		// Doit afficher "Nouveau compte n° : 1 appartenant a : Jean Neymar"
		System.out.println("Nouveau compte n° : " + c1.getNumeroCompte() + " appartenant a : " + c1.getPersonne());
		
		System.out.println();
		
		// Doit afficher toutes les informations du compte correctement initialisées
		Compte c2 = new CompteBancaire(1, 1000, 500, new Personne("Morisse", "Pierre"));
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
		
		// Doit afficher un message d'erreur
		c2.debiter(400);
		
		System.out.println();
		
		// Doit afficher 300.0
		System.out.println(c2.consulterSolde());
		
		System.out.println();
		
		c2.debiter(300);
		// Doit afficher 0.0
		System.out.println(c2.consulterSolde());
	}
}
