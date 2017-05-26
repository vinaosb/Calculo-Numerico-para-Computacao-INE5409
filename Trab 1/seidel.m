function seidel(A)
% Metodo iterativo de Gauss-Seidel
% Otimizacao do jacobi mas ele usa uma variavel calculada dentro da equacao seguinte numa mesma iteracao usando um fator de relaxacao para evitar a oscilacao

n = 15
% i = 1 >> x(i) + 4x(i+1) = 5
% i = 2:n-1  >> x(i-1) + x(i) = -1
% i = n >> x(i-1) + x(i) = -1

% valor inical antes das iterações
x = zeros(1,n);



% diferença entre xInicial e x
dif = 1;
% tolerancia, limite de parada do programa, precisão entre os valores calculados
tol = 1e-4;
% limite de iteracoes
limite = 10000;
% iteracao atual
k= 0;

% O metodo de Gauss Seidel pode oscilar devido a grande diferença entre o valor calculado e o novo (Delta), e para isso um  
% valor de amortecimento, relaxação (lambda) pode ser usado para reduzir essa mudança drástica
lambda = 1.5;

while (dif > tol && k < limite)
  xInicial = x;

% formulas dadas do sistema, seidel usa o proprio valor calculado na iteracao
% -------------------------------Seidel com Relaxacao
   i = 1;
   x(i) = (1 - lambda) * x(i) + lambda*(5 -4*x(i+1))/1;
   for i = 2:n-1
      x(i) = (1 - lambda) * x(i) + lambda*(3 - x(i-1) - x(i+1))/1;
   end
   i = n;
   x(3) = (1 - lambda) * x(i) + lambda*(-1 - x(i-1))/1;


%--------------------------------Seidel sem relaxacao    
%   x(1) = (1 + x(2) + x(3))/3;
%   x(2) = (5 - x(1) - x(3))/3;
%   x(3) = (4 - 2*x(1) + 2 * x(2))/4;
    
% diferença entre o valor anterior e o calculado, pega o maior deles
% este valor é dividido pelo .x para demonstrar de forma otimizada o erro se as diferenças forem muito grandes ou muito pequenas
    dif = max(abs( (xInicial .-x) ));
    
    xInicial = x;
    
%%    printf("k => Iteração nº %d \n",k);
%%    printf("Diferença entre xInicial e X = %e \n\n", dif);
    k++;
end

%Resultados
printf("Solução obtida após %d iterações:\n", k);
x

% Erro = Valor Aproximado - Valor Exato
xExato = [1, 1, 1];
printf("Erro de Truncamento: \n");
erroTruncamento = max(abs(x .- xExato))

end


