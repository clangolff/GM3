import java.util.List;
import java.util.ArrayList;

public class Personne {
	
	private String nom;
	private String prenom;
	private ArrayList<Compte> Comptes = new ArrayList<Compte>(); 	
	
	
	public Personne() {
		this.nom = "";
		this.prenom = "";
		this.Comptes = null;
	}
	
	public Personne(String nom, String prenom, ArrayList<Compte> comptes) {
		this.nom = nom;
		this.prenom = prenom;
		this.Comptes = comptes;
	}
	
	public String getNom() {
		return this.nom;
	}
	
	public String getPrenom() {
		return this.prenom;
	}
	
	public void setNom(String nom) {
		this.nom = nom;
	}
	
	public void setPrenom(String prenom) {
		this.prenom = prenom;
	}
	
    public String toString() {
		return prenom + "\t" + nom;
	}
	
	public boolean equals(Object o) {
		if (o == null || o.getClass() != this.getClass()) {
			return false;
		}
		
		Personne p = (Personne) o;
		return p.getPrenom().equals(this.getPrenom()) && p.getNom().equals(this.getNom());
	}
	
	public int hashCode() {
		return 7 * nom.hashCode() + 13 * prenom.hashCode();
	}

	public ArrayList<Compte> getComptes(){
		return this.Comptes;
	}

	public void setComptes(ArrayList<Compte> comptes) {
		this.Comptes = comptes;
	} 

	public void ajouterCompte(Compte compte) {
		if (!(this.Comptes.contains(compte))){
			this.Comptes.add(compte);
		}
	}

	void supprimerCompte(Compte compte){
		if (this.Comptes.contains(compte)){
			this.Comptes.remove(compte);
		}
	}
}
