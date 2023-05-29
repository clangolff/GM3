program repres;
const MAX_ITER = 400;
var i : integer;
    x : extended;
//    x : real;

begin
    x := 1;
    for i := 1 to MAX_ITER do
    begin
        x := x/10;
//        writeln(i, 1.+x)
        writeln(i, x)
    end;
end.

