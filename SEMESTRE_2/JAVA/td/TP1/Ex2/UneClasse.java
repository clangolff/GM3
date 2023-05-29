public class UneClasse {

    public UneClasse() {

    }

    public boolean estPair(int i){
    	return (i % 2) == 0;
    }

    public void typeOperation(char c){
	switch(c){
		case '+': 
			System.out.println("c'est une addition");
			break;
		case '-': 
			System.out.println("c'est une soustraction");
			break;
		case '/': 
			System.out.println("c'est une division");
			break;
		case '*': 
			System.out.println("c'est une multiplication");	
			break;
		default :  
			System.out.println("drole d'expression");
		       	break;
	}	
    }
}
