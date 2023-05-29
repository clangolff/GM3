import java.util.Set;
import java.util.HashSet;
import java.io.PrintWriter;
import java.io.FileNotFoundException;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Arrays;
import java.io.Serializable;

public class Banque implements BanqueInt, Serializable {  
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
	  comptesCourants.add(compte);
	  compte.getPersonne().ajouterCompte(compte);
  }
  
  public void ajouterCompte(CompteEpargne compte) {
	  comptesEpargne.add(compte);
	  compte.getPersonne().ajouterCompte(compte);
  }
  
  public boolean estPresent(CompteCourant compte) {
	  return comptesCourants.contains(compte);  
  }
  
  public boolean estPresent(CompteEpargne compte) {
	  return comptesEpargne.contains(compte);
  }
  
  public int nombreDeComptes() {
	  return comptesCourants.size() + comptesEpargne.size();
  }
  
  public void supprimerCompte(CompteCourant compte) {
	  comptesCourants.remove(compte);
	  compte.getPersonne().supprimerCompte(compte);
  }
  
  public void supprimerCompte(CompteEpargne compte) {
	  comptesEpargne.remove(compte);
	  compte.getPersonne().supprimerCompte(compte);
  }
  
  public String toString() {
	  return "La banque : " + nomBanque + " située a " + adresseBanque + " possede " + nombreDeComptes() + " comptes.";
  }

}
