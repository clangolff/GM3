clear all;

exp1 = exp(1);
expNeg1 = 1/exp1;

I0 = exp1-expNeg1;
I1 = 0;
n = 20;

fprintf('I0 = %f\n',I0);

for i=1:n
    I1 = i * I0 - expNeg1 + ((-1)^i) * exp1;
    I0 = I1;
    fprintf("I%d = %f\n", i, I0);
end
