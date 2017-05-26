function thomas()
n=15
% i = 1 >> x(i) + 4x(i+1) = 5
% i = 2:n-1  >> x(i-1) + x(i) = -1
% i = n >> x(i-1) + x(i) = -1


i = 1;
t(i) = NaN;
r(i) = 1;
d(i) = 4;
b(i) = 5;
for i = 2:n-1
  t(i) = 1;
  r(i) = 1;
  d(i) = 0;
  b(i) = -3;
end
i = n;
t(i) = 1;
r(i) = 1;
d(i) = NaN;
b(i) = -1;


%Escalonamento: 
     for i=2:n 
          aux=t(i)/r(i-1); 
          r(i)=r(i)-aux*d(i-1); 
          b(i)=b(i)-aux*b(i-1); 
          t(i)=0;     
     end 
%Retrosubstituicoes: 
     x(n)=b(n)/r(n); 
     for i=n-1:-1:1 
          x(i)=(b(i)-d(i)*x(i+1))/r(i); 
     end 
     t
     r
     d
     b
x 