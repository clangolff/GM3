public class TestEquals {
	
	public static void main(String[] args) {
		Compte c1 = new CompteCourant(2, 1000, 500, new Personne("Morisse", "Pierre"), 100);
		Compte c2 = new CompteCourant(2, 1000, 500, new Personne("Morisse", "Pierre"), 100);
		
		System.out.println("c1 == c2 : " + (c1 == c2));
		System.out.println("c1.equals(c2) : " + c1.equals(c2));
		System.out.println("c2.equals(c1) : " + c2.equals(c1));
		
		System.out.println("c1.getCredit() == c2.getCredit() : " + (c1.getCredit() == c2.getCredit()));
		System.out.println("c1.getDebit() == c2.getDebit() : " + (c1.getDebit() == c2.getDebit()));
		System.out.println("c1.getNumeroCompte() == c2.getNumeroCompte() : " + (c1.getNumeroCompte() == c2.getNumeroCompte()));
		System.out.println("c1.getPersonne().equals(c2.getPersonne() : " + c1.getPersonne().equals(c2.getPersonne()));
		System.out.println("c2.getPersonne().equals(c1.getPersonne() : " + c2.getPersonne().equals(c1.getPersonne()));
	}
}
