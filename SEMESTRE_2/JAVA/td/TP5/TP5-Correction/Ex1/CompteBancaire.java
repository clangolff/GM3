public abstract class CompteBancaire implements Compte {
	private int numeroCompte;
	private double credit;
	private double debit;
	private Personne personne;
	
	public CompteBancaire() {
		this.numeroCompte = 0;
		this.credit = 0;
		this.debit = 0;
		this.personne = new Personne();
	}
	
	public CompteBancaire(int numeroCompte, double credit, double debit, Personne personne) {
		this.numeroCompte = numeroCompte;
		this.credit = credit;
		this.debit = debit;
		this.personne = personne;
	}
	
	public double getCredit() {
		return this.credit;
	}
	
	public double getDebit() {
		return this.debit;
	}
	
	public int getNumeroCompte() {
		return this.numeroCompte;
	}
	
	public Personne getPersonne() {
		return this.personne;
	}
	
	public void setCredit(double credit) {
		this.credit = credit;
	}
	
	public void setDebit(double debit) {
		this.debit = debit;
	}
	
	public void setNumeroCompte(int numeroCompte) {
		this.numeroCompte = numeroCompte;
	}
	
	public void setPersonne (Personne personne) {
		this.personne = personne;
	}
	
	public double consulterSolde() {
		return credit - debit;
	}
	
	public void crediter(double montant) {
		this.credit = this.credit + montant;
	}
	
	public abstract void debiter(double montant) throws DebitImpossible;
	
	public boolean equals(Object o) {
		if (o == null || o.getClass() != this.getClass()) {
			return false;
		}
		
		CompteBancaire c = (CompteBancaire) o;
		return c.getCredit() == this.getCredit() && c.getDebit() == this.getDebit() && c.getNumeroCompte() == this.getNumeroCompte() && c.getPersonne().equals(this.getPersonne());
	}
	
	public int hashCode() {
		return (int) (1 * credit + 3 * debit + 5 * numeroCompte + 7 * personne.hashCode());
	}
}
