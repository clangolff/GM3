public class TestExceptions {
	
	public static int division(int a, int b) throws ArithmeticException {		
		if (b == 0){
			throw new ArithmeticException("tu veux du pain ?");
		} else {
		return a / b;
		}
	}

	public static void main(String[] args) {
		System.out.println("Un print avant l'exception");
		
        int r = division(54, 0);
		
		System.out.println("Un print apres l'exception");
	}
	
}
