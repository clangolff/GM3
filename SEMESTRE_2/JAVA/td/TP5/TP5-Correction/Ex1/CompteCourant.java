public class CompteCourant extends CompteBancaire {
	private double decouvertMax;
	
	public CompteCourant() {
		super();
		this.decouvertMax = 0;
	}
	
	public CompteCourant(int numeroCompte, double credit, double debit, Personne personne, double decouvertMax) {
		super(numeroCompte, credit, debit, personne);
		this.decouvertMax = decouvertMax;
	}
	
	public double getDecouvertMax() {
		return this.decouvertMax;
	}
	
	public void setDecouvertMax(double decouvertMax) {
		this.decouvertMax = decouvertMax;
	}
	
	public void debiter(double montant) throws DebitImpossible {
		if (getCredit() - getDebit() - montant + decouvertMax >= 0) {
			setDebit(getDebit() + montant);
		} else {
			throw new DebitImpossible();
		}
	}
	
	public String toString() {
		return getNumeroCompte() + "\t" + getCredit() + "\t" + getDebit() + "\t" + getPersonne() + "\t" + this.decouvertMax;
	}

	public boolean equals(Object o) {		
		if (o == null || o.getClass() != this.getClass()) {
			return false;
		}
		
		boolean b = super.equals(o);
		CompteCourant c = (CompteCourant) o;
		return b && c.getDecouvertMax() == this.getDecouvertMax();
	}
	
	public int hashCode() {
		return (int) (super.hashCode() + 9 * decouvertMax);
	}

}
