      double precision function dcch(x)  
      use modcch
      implicit none
      double precision x

      dcch =  -w*sin(x)*cosh(x) + w*cos(x)*sinh(x)
 
      end
