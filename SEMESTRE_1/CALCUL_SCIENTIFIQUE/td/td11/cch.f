      double precision function cch(x)  
      use modcch
      implicit none
      double precision x

      cch = 1.d0 + w*cos(x)*cosh(x)
 
      end
