import java.util.List;
import java.util.ArrayList;

public abstract class CompteBancaire implements Compte{
	private Personne p;
	private double soldeCredit;
	private double soldeDebit;
	private int NumeroCompte;

	public CompteBancaire(){
		this.p = new Personne();
		this.soldeCredit = 0;
		this.soldeDebit = 0;
		this.NumeroCompte = 0;
	}

	public CompteBancaire(int idcompte, double credit, double debit, Personne p){
	this.p = p;
	this.NumeroCompte = idcompte;
	this.soldeCredit = credit;
	this.soldeDebit = debit;
	}

	public void setCredit(double credit){
		this.soldeCredit = credit;
	}

	public double getCredit(){
		return  this.soldeCredit;
	}

	public void setDebit(double debit){
		this.soldeDebit = debit;
	}

	public double getDebit(){
		return this.soldeDebit;
	}

	public void setNumeroCompte(int numeroCompte){
		this.NumeroCompte = numeroCompte;
	}

	public int getNumeroCompte(){
		return this.NumeroCompte;
	}

	public double consulterSolde(){
		return -this.soldeDebit + this.soldeCredit;
	}

	public void crediter(double montant){
		this.soldeCredit += montant;
	}

	public abstract void debiter(double montant);

	public void setPersonne(Personne p){
		this.p = p;
	}

	public Personne getPersonne(){
		return this.p;
	}

	public String toString(){
		return this.p.toString() + "\t" + this.NumeroCompte + "\t" + this.soldeCredit + "\t" + this.soldeDebit;
	}

	public boolean equals(Object o){
		if (o == null || o.getClass() != this.getClass()){
			return false;
		}
		CompteBancaire CB = (CompteBancaire) o;
		return CB.getPersonne().equals(this.getPersonne()) && (CB.getCredit() == this.getCredit()) && ( CB.getDebit() == this.getDebit() ) && ( CB.getNumeroCompte() == this.getNumeroCompte() ) && ( CB.getCredit() == this.getCredit());
	}

	public int hashcode() {
		return 5*p.hashCode()+2*Double.hashCode(soldeCredit)+2*Double.hashCode(soldeDebit)+Integer.hashCode(NumeroCompte); 
	
	}

}
