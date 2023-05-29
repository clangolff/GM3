public class UnProgramme {

	public static void main(String[] args) {
		UneClasse pc = new UneClasse();
		
		System.out.println(pc.estPair(24));
		pc.typeOperation('+');

		for (int i=0;i<11;i++){
			System.out.println(i + "est pair " +pc.estPair(i));
		}
		
		int u = 0;
		while(u<1000) {
			System.out.println(u);
			u = 2 * u + 3;
		}
	}

}
