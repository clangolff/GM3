public class TestBanqueExceptions {
	
	public static void main(String[] args) {
		Compte c1 = new CompteCourant(1, 500, 0, new Personne("Morisse", "Pierre"), 0);
		try{
		c1.debiter(501);
		}
		catch (DebitImpossible d){
			System.out.println("Tu l'as dans l'os");
		}
		Compte c2 = new CompteEpargne(2, 200, 100, new Personne("Morisse", "Pierre"), 0.5);
		try{
		c2.debiter(150);
		}
		catch(DebitImpossible d){
			System.out.println("tu l'as dans l'os");
		}
	}
}
