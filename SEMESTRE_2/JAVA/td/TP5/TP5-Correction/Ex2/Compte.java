public interface Compte {
	
	public double getCredit();
	public double getDebit();
	public int getNumeroCompte();
	public Personne getPersonne();
	
	public void setCredit(double credit);	
	public void setDebit(double debit);
	public void setNumeroCompte(int numeroCompte);
	public void setPersonne (Personne personne);
	
	public double consulterSolde();
	public void crediter(double montant);
	public void debiter(double montant) throws DebitImpossible;
}
