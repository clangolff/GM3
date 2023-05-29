import java.util.Set;
import java.util.HashSet;
import java.io.Writer;
import java.io.FileWriter;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Arrays;

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
  
  public void charger(String file) {
	  String line;
	  int nbComptesCourant;
	  int nbComptesEpargne;
	  String[] s;
	  
	  try {
		  FileReader fileReader = new FileReader(file);
		  BufferedReader bufferedReader = new BufferedReader(fileReader);
		  
		  // Adresse banque
		  line = bufferedReader.readLine();
		  adresseBanque = line;
		  
		  // Nom banque
		  line = bufferedReader.readLine();
		  nomBanque = line;
		  
		  // Nombre comptes courant
		  line = bufferedReader.readLine();
		  nbComptesCourant = Integer.parseInt(line);
		  for (int i = 0; i < nbComptesCourant; i++) {
			  line = bufferedReader.readLine();
			  s = line.split("\t");
			  ajouterCompte(new CompteCourant(Integer.parseInt(s[0]), Double.parseDouble(s[1]), Double.parseDouble(s[2]), new Personne(s[3], s[4]), Double.parseDouble(s[5])));
		  }
		  
		  // Nombre comptes courant
		  line = bufferedReader.readLine();
		  nbComptesEpargne = Integer.parseInt(line);
		  for (int i = 0; i < nbComptesEpargne; i++) {
			  line = bufferedReader.readLine();
			  s = line.split("\t");
			  ajouterCompte(new CompteEpargne(Integer.parseInt(s[0]), Double.parseDouble(s[1]), Double.parseDouble(s[2]), new Personne(s[3], s[4]), Double.parseDouble(s[5])));
		  }
	  } catch (Exception e) {
		  System.out.println("Erreur de chargement : " + e);
	  }
  }
  
  public void enregistrer(String file) {
	  try {
		  Writer fWriter = new FileWriter(file);
		  BufferedWriter bWriter = new BufferedWriter(fWriter);
		  bWriter.write(adresseBanque);
		  bWriter.newLine();
		  bWriter.write(nomBanque);
		  bWriter.newLine();
		  
		  bWriter.write(String.valueOf(comptesCourants.size()));
		  bWriter.newLine();
		  
		  for (CompteCourant c : comptesCourants) {
			  bWriter.write(c.toString());
			  bWriter.newLine();
		  }
		  
		  bWriter.write(String.valueOf(comptesEpargne.size()));
		  bWriter.newLine();
		  
		  for (CompteEpargne c : comptesEpargne) {
			  bWriter.write(c.toString());
			  bWriter.newLine();
		  }
		  
		  bWriter.close();
		  fWriter.close();
	  } catch (Exception e) {
		  System.out.println("Erreur d'enregistrement" + e);
	  }
  }
  
  public String toString() {
	  return "La banque : " + nomBanque + " située a " + adresseBanque + " possede " + nombreDeComptes() + " comptes.";
  }

}
