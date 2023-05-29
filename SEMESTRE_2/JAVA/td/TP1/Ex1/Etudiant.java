public class Etudiant extends Personne{
	private String promo;

	public Etudiant(){
		super();
		this.promo = "";
	}

	public Etudiant(String Prenom, String Nom, String Promo){
		super(Prenom,Nom);
		this.promo = Promo;
	}

	public String toString(){
		return super.toString() +  " je suis en promo " + this.promo; 
	}
}
