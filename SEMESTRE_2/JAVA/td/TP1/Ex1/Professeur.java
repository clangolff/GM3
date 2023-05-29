public class Professeur extends Personne{
	private double salaire;

	public Professeur(){
		super();
		this.salaire = 0;
	}

	public Professeur(String Prenom, String Nom, double salaire){
		super(Prenom,Nom);
		this. salaire =  salaire;
	}

	public String toString(){
		return super.toString() + " je gagne " + this. salaire; 
	}
}
