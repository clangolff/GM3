public class TestPolymorphisme {

	public static void main(String[] args) {
		Personne n = new Personne("Neymar", "Jean");
		Personne p = new Professeur("Morisse", "Pierre", 150000);
		Personne e = new Etudiant("Dupont", "Jean", "GM3");
		
		System.out.println(n);
		System.out.println(p);
		System.out.println(e);
	}

}
