public class TestHeritage {
	public static void main(String[] args) {
		Etudiant E1 = new Etudiant("clement","lnglff","GM3");
		System.out.println(E1.toString());

		Professeur P1 = new Professeur("dudu", "le roi",200);
		System.out.println(P1.toString());
		System.out.println(P1);
	}	
}
