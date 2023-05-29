public class CompteCourant extends CompteBancaire{
	private double decouvertMax;

	public CompteCourant(){
		super();
		this.decouvertMax = 0;
	}

	public CompteCourant(int idcompte, double credit, double debit, Personne p, double decouvertMax){
		super(idcompte,credit,debit,p);
		this.decouvertMax = decouvertMax;
	}

	public void setDecouvertMax(double Max){
		this.decouvertMax = Max;
	}

	public double getDecouvertMax(){
		return this.decouvertMax;
	}

	public void debiter(double montant){
		double soldeCredit = getCredit();
		if ( soldeCredit + this.decouvertMax > montant){
			double soldeDebit = getDebit();
			setDebit(soldeDebit + montant);
		}
		else {
			System.out.println("tu l'as dans l'os");
		}	
	}

	public String toString(){
		return super.toString() + "\t" + this.decouvertMax;
	}
}
