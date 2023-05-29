public interface Compte {

	public void setCredit(double credit);
	public double getCredit();
	public void setDebit(double debit);
	public double getDebit();
	
	public void setNumeroCompte(int numeroCompte);
	public int getNumeroCompte();	
	public double consulterSolde();
	public void crediter(double montant);
	public void debiter(double montant) throws DebitImpossible;
	public void setPersonne(Personne p);
	public Personne getPersonne();

}
