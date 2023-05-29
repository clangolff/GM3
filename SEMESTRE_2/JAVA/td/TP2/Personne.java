public class Personne{
	private String nom;
	private String prenom;

	public Personne(){
		this.nom = "";
		this.prenom = "";
	}

	public Personne(String Prenom, String Nom){
		this.nom = Nom;
		this.prenom = Prenom;
	}

	public String getNom(){
		return this.nom;
	}

	public String getPrenom(){
		return this.prenom;
	}

	public void setNom(String nom){
		this.nom = nom;	
	}

	public void setPrenom(String prenom){
		this.prenom = prenom;
	}

	public String toString(){
		return this.prenom + " " + this.nom;
	} 
}
