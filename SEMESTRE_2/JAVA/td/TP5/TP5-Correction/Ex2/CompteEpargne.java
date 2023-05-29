import java.io.Serializable;

public class CompteEpargne extends CompteBancaire {
	private double tauxInterets;
	
	public CompteEpargne() {
		super();
		this.tauxInterets = 0;
	}
	
	public CompteEpargne(int numeroCompte, double credit, double debit, Personne personne, double tauxInterets) {
		super(numeroCompte, credit, debit, personne);
		this.tauxInterets = tauxInterets;
	}
	
	public double getTauxInterets() {
		return this.tauxInterets;
	}
	
	public void setTauxInterets(double tauxInterets) {
		this.tauxInterets = tauxInterets;
	}
	
	public void debiter(double montant) throws DebitImpossible {
		if (getCredit() - getDebit() - montant >= 0) {
			setDebit(getDebit() + montant);
		} else {
			throw new DebitImpossible();
		}
	}
	
	public double calculerInterets() {
		return (double) tauxInterets * consulterSolde();
	}
	
	public String toString() {
		return getNumeroCompte() + "\t" + getCredit() + "\t" + getDebit() + "\t" + getPersonne() + "\t" + this.tauxInterets;
	}
	
	public boolean equals(Object o) {		
		if (o == null || o.getClass() != this.getClass()) {
			return false;
		}
		
		boolean b = super.equals(o);
		CompteEpargne c = (CompteEpargne) o;
		return b && c.getTauxInterets() == this.getTauxInterets();
	}
	
	public int hashCode() {
		return (int) (super.hashCode() + 9 * tauxInterets);
	}
}
