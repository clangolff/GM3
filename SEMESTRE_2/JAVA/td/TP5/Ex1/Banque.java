import java.util.Set;
import java.util.HashSet;
import java.io.*;
import java.util.Iterator;

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

  public void charger(String file){
  try{
	BufferedReader fichier = new BufferedReader(new FileReader(file));
	this.nomBanque = fichier.readLine();
	this.adresseBanque = fichier.readLine();
	int nCourant = Integer.parseInt(fichier.readLine());
	for(int i=0;i<nCourant;i++){
		String s = fichier.readLine();
		String[] tab = s.split("\t");

		String prenom = tab[0];
		String nom = tab[1];
		int idCompte = Integer.parseInt(tab[2]);
		double credit = Double.parseDouble(tab[3]);
		double debit = Double.parseDouble(tab[4]);
		double decouvertMax = Double.parseDouble(tab[5]);
		
		Personne p = new Personne(nom,prenom);
		CompteCourant c = new CompteCourant(idCompte,credit,debit,p,decouvertMax);
		ajouterCompte(c);
		}
	int nEpargne = Integer.parseInt(fichier.readLine());
	for(int i=0;i<nEpargne;i++){
		String s = fichier.readLine();
		String[] tab = s.split("\t");

		String prenom = tab[0];
		String nom = tab[1];
		int idCompte = Integer.parseInt(tab[2]);
		double credit = Double.parseDouble(tab[3]);
		double debit = Double.parseDouble(tab[4]);
		double tauxInteret = Double.parseDouble(tab[5]);
		
		Personne p = new Personne(nom,prenom);
		CompteEpargne c = new CompteEpargne(idCompte,credit,debit,p,tauxInteret);
		ajouterCompte(c);
		}
  	}
  catch(FileNotFoundException e){
  	e.printStackTrace();
  	}
  catch(IOException e){
  	e.printStackTrace();
  	}
  }
  
  public void enregistrer(String file){
	try{
	BufferedWriter fichier = new BufferedWriter(new FileWriter(file));
	/* attribut de la banque*/
	fichier.write(this.adresseBanque);
	fichier.newLine();
	fichier.write(this.nomBanque);
	fichier.newLine();
	
	/* nombre de compte courant */
	int nCourant = this.comptesCourants.size();
	fichier.write(String.valueOf(nCourant));
	fichier.newLine();
	for(CompteCourant c :  this.comptesCourants){
		fichier.write(c.toString());
		fichier.newLine();
		} 
	

	/* nombre de compte epargne */
	int nEpargne = this.comptesEpargne.size();
	fichier.write(String.valueOf(nEpargne));
	fichier.newLine();
	for(CompteEpargne c : this.comptesEpargne){
		fichier.write(c.toString());
		fichier.newLine();
		}
	fichier.close();
		}
	catch(FileNotFoundException e) {
		e.printStackTrace();
		}
	catch(IOException e){
		e.printStackTrace();
		}
	}
}
