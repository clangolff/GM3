import java.util.Set;

public interface BanqueInt {  
  public String getAdresseBanque();
  public String getNomBanque();
  public Set<CompteCourant> getComptesCourants();
  public Set<CompteEpargne> getComptesEpargne();
  
  public void setAdresseBanque(String adresseBanque);
  public void setNomBanque(String nomBanque);
  public void setComptesCourants(Set<CompteCourant> comptesCourants);
  public void setComptesEpargne(Set<CompteEpargne> comptesEpargne);
    
  // Ajoute le compte compte à l'ensemble de CompteCourant de la Banque.
  // Si le compte est déjà présent, il ne devra pas y être ajouté à nouveau.
  public void ajouterCompte(CompteCourant compte);
  
  // Ajoute le compte compte à l'ensemble de CompteEpargne de la Banque.
  // Si le compte est déjà présent, il ne devra pas y être ajouté à nouveau.
  public void ajouterCompte(CompteEpargne compte);
  
  // Vérifie la présence du compte compte au sein de l'ensemble de CompteCourant de la Banque.
  // Retourne true si le compte y est présent, et false sinon.
  public boolean estPresent(CompteCourant compte);
  
  // Vérifie la présence du compte compte au sein de l'ensemble de CompteEpargne de la Banque.
  // Retourne true si le compte y est présent, et false sinon.
  public boolean estPresent(CompteEpargne compte);
  
  // Retourne le nombre total de comptes présents au sein de la Banque, qu'il s'agisse
  // de CompteCourant ou de CompteEpargne.
  public int nombreDeComptes();
  
  // Supprime le compte compte de l'ensemble de CompteCourant de la Banque.
  // Ne doit pas provoquer d'erreur si le compte n'est pas initialement présent dans l'ensemble.
  public void supprimerCompte(CompteCourant compte);
  
  // Supprime le compte compte de l'ensemble de CompteCourant de la Banque.
  // Ne doit pas provoquer d'erreur si le compte n'est pas initialement présent dans l'ensemble.
  public void supprimerCompte(CompteEpargne compte);

}
