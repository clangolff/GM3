public class TestPersonne {

	public static void main(String[] args) {
		Personne p1 = new Personne();
		System.out.println(p1.toString());
        System.out.println("Nom : " + p1.getNom());
        System.out.println("Prenom : " + p1.getPrenom());
		p1.setNom("Dupont");
		System.out.println("Nouveau nom : " + p1.getNom());
		p1.setPrenom("Jean");
		System.out.println("Nouveau prenom : " + p1.getPrenom());
		System.out.println(p1);
		
		Personne p2 = new Personne("Bob", "Leponge");
        System.out.println("Nom : " + p2.getNom());
        System.out.println("Prenom : " + p2.getPrenom());
		System.out.println(p2);
	}

}
