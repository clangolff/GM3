public class CompteEpargne extends CompteBancaire{
	private double taux_interet;

	public CompteEpargne(){
		super();
		this.taux_interet = 0;
	}

	public CompteEpargne(int idcompte, double credit, double debit, Personne p, double taux_interet){
		super(idcompte,credit,debit,p);
		this.taux_interet = taux_interet;
	}

	public void setTauxInterets(double taux){
		this.taux_interet = taux;
	}

	public double getTauxInterets(){
		return this.taux_interet;
	}

	public void debiter(double montant) throws DebitImpossible{
		double solde = super.consulterSolde();
		if ( Math.abs(solde - montant) < 10e-7 ){
			throw new DebitImpossible("tu l'as dans l'os");
		}
		else{
		        double SoldeDebit = super.getDebit();
			super.setDebit(SoldeDebit + montant);
		}	
	}

	public double calculerInterets(){
		double solde = super.consulterSolde();
		return solde * this.taux_interet;
	}

	public String toString(){
		return super.toString() + "\t" + this.taux_interet;
	}

	public boolean equals(Object o){
                if (o == null || o.getClass() != this.getClass()){
                        return false;
                }
                CompteEpargne CB = (CompteEpargne) o;
                return super.equals(CB) && ( CB.getTauxInterets() == this.getTauxInterets() );
        }

        public int hashcode() {
                return super.hashCode()+2*Double.hashCode(taux_interet);
        }


}