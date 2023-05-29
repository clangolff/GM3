c*****************
c eqt second degre
c************

      program eq
      implicit none
      real a,b,c ,x1,x2,d,ta

      read(*,*) a,b,c

      d = b**2-4.*a*c
      if (d < 0.) then
         stop
      else
         d = sqrt(d)
      endif
      ta = 2.*a

      if( b < 0.  ) then
        x1 = (-b +d)/ta
      else
        x1 = (-b -d)/ta
      endif
      x2 = c/(a*x1)
      write(*,*) 'avec precautions  ',x1,x2
      x1 = (-b +d)/ta
      x2 = (-b -d)/ta
      write(*,*) 
      write(*,*) 'sans precautions  ',x1,x2
      
      end
