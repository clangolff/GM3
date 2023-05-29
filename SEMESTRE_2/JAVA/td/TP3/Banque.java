import java.util.Set;
import java.util.HashSet;

public class Banque implements BanqueInt {  
  private String adresseBanque;
  private String nomBanque;
  private Set<CompteCourant> comptesCourants;
  private Set<CompteEpargne> comptesEpargne;
  
  public Banque() {
	  this.adresseBanque = "";
	  this.nomBanque = "";
	  this.comptesCourants = new HashSet<CompteCourant>();
	  this.comptesEpargne = new HashSet<CompteEpargne>();
  }
  
  public Banque (String adresseBanque, String nomBanque) {
	  this.adresseBanque = adresseBanque;
	  this.nomBanque = nomBanque;
	  this.comptesCourants = new HashSet<CompteCourant>();
	  this.comptesEpargne = new HashSet<CompteEpargne>();
  }
  
  public Banque (String adresseBanque, String nomBanque, Set<CompteCourant> comptesCourants, Set<CompteEpargne> comptesEpargne) {
	  this.adresseBanque = adresseBanque;
	  this.nomBanque = nomBanque;
	  this.comptesCourants = comptesCourants;
	  this.comptesEpargne = comptesEpargne;
  }
  
  public String getAdresseBanque() {
	  return this.adresseBanque;
  }
  
  public String getNomBanque() {
	  return this.nomBanque;
  }
  
  public Set<CompteCourant> getComptesCourants() {
	  return this.comptesCourants;
  }
  
  public Set<CompteEpargne> getComptesEpargne() {
	  return this.comptesEpargne;
  }
  
  public void setAdresseBanque(String adresseBanque) {
	  this.adresseBanque = adresseBanque;
  }
  
  public void setNomBanque(String nomBanque) {
	  this.nomBanque = nomBanque;
  }
  
  public void setComptesCourants(Set<CompteCourant> comptesCourants) {
	  this.comptesCourants = comptesCourants;
  }
  
  public void setComptesEpargne(Set<CompteEpargne> comptesEpargne) {
	  this.comptesEpargne = comptesEpargne;
  }
  
  public void ajouterCompte(CompteCourant compte) {
	this.comptesCourants.add(compte);
	Personne p = compte.getPersonne();
	p.ajouterCompte(compte);	
  }
  
  public void ajouterCompte(CompteEpargne compte) {
	  this.comptesEpargne.add(compte);
	  Personne p = compte.getPersonne();
	  p.ajouterCompte(compte);
  }
  
  public boolean estPresent(CompteCourant compte) {
	  return this.comptesCourants.contains(compte);
  }
  
  public boolean estPresent(CompteEpargne compte) {
	  return this.comptesEpargne.contains(compte);
  }
  
  public int nombreDeComptes() {
	  return this.comptesCourants.size() + this.comptesEpargne.size();
  }
  
  public void supprimerCompte(CompteCourant compte) {
	  this.comptesCourants.remove(compte);
	  Personne p = compte.getPersonne();
	  p.supprimerCompte(compte);
  }
  
  public void supprimerCompte(CompteEpargne compte) {
	  this.comptesEpargne.remove(compte);
	  Personne p = compte.getPersonne();
	  p.supprimerCompte(compte);
  }
  
  public String toString() {
	  return "La banque : " + nomBanque + " située a " + adresseBanque + " possede " + nombreDeComptes(); 
  }

}
