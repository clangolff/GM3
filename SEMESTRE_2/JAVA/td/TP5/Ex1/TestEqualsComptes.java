public class TestEqualsComptes {
	
	public static void main(String[] args) {		
		CompteCourant c1 = new CompteCourant(2, 1000, 500, new Personne("Morisse", "Pierre"), 100);
		CompteCourant c2 = new CompteCourant(2, 1000, 500, new Personne("Morisse", "Pierre"), 500);
		
		System.out.println("c1.equals(c2) : " + (c1.equals(c2)));
		System.out.println("c2.equals(c1) : " + (c2.equals(c1)));
		
		CompteEpargne c3 = new CompteEpargne(2, 1000, 500, new Personne("Morisse", "Pierre"), 0.05);
		CompteEpargne c4 = new CompteEpargne(2, 1000, 500, new Personne("Morisse", "Pierre"), 0.10);
		
		
		System.out.println("c3.equals(c4) : " + (c3.equals(c4)));
		System.out.println("c4.equals(c3) : " + (c4.equals(c3)));
		
		c2.setDecouvertMax(100);
		c3.setTauxInterets(0.10);
		
		System.out.println("c1.equals(c2) : " + (c1.equals(c2)));
		System.out.println("c3.equals(c4) : " + (c3.equals(c4)));		
	}
}
