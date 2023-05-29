import java.util.List;
import java.util.ArrayList;
import java.io.Serializable;

public class Personne implements Serializable {
	
	private String nom;
	private String prenom;
	private List<Compte> comptes;
	
	public Personne() {
		this.nom = "";
		this.prenom = "";
		this.comptes = new ArrayList<Compte>();
	}

    public Personne(String nom, String prenom) {
        this.nom = nom;
        this.prenom = prenom;
        this.comptes = new ArrayList<Compte>();
    }
	
	public Personne(String nom, String prenom, List<Compte> comptes) {
		this.nom = nom;
		this.prenom = prenom;
		this.comptes = comptes;
	}
	
	public List<Compte> getComptes() {
		return this.comptes;
	}
	
	public String getNom() {
		return this.nom;
	}
	
	public String getPrenom() {
		return this.prenom;
	}
	
	public void setComptes(List<Compte> comptes) {
		this.comptes = comptes;
	}
	
	public void setNom(String nom) {
		this.nom = nom;
	}
	
	public void setPrenom(String prenom) {
		this.prenom = prenom;
	}
	
	public void ajouterCompte(Compte compte) {
		if (!comptes.contains(compte)) {
			comptes.add(compte);
		}
	}
	
	public void supprimerCompte(Compte compte) {
		if (comptes.contains(compte)) {
			comptes.remove(compte);
		}
	}
	
    public String toString() {
		return nom + "\t" + prenom;
	}
	
	public boolean equals(Object o) {
		if (o == null || o.getClass() != this.getClass()) {
			return false;
		}
		
		Personne p = (Personne) o;
		return p.getPrenom().equals(this.getPrenom()) && p.getNom().equals(this.getNom());
	}
	
	public int hashCode() {
		return 42 * nom.hashCode() + 13 * prenom.hashCode();
	}

}
