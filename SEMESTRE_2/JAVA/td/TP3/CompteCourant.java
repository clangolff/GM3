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
		double solde = super.consulterSolde();
		if ( solde - montant < this.decouvertMax ){
			System.out.println("tu l'as dans l'os");
		}
		else{
			double SoldeDebit = super.getDebit();
			super.setDebit(SoldeDebit + montant);
		}	
	}

	public String toString(){
		return super.toString() + "\t" + this.decouvertMax;
	}
	
	public boolean equals(Object o){
                if (o == null || o.getClass() != this.getClass()){
                        return false;
                }
                CompteCourant CB = (CompteCourant) o;
                return super.equals(CB) && ( CB.getDecouvertMax() == this.getDecouvertMax() );
        }

	public int hashcode() {
		return super.hashCode()+2*Double.hashCode(decouvertMax);
	}



}
