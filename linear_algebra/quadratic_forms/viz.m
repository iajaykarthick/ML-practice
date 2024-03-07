% Linear Form Visualization
A = [4 18]; % Example matrix for linear form
x = -2:.1:2; % Range of values for the vector component

linearForm = zeros(size(x));
for i = 1:length(x)
    for j = 1: length(x)
        % Define the vector component for this iteration
        v = [x(i); x(j)];
        
        % Compute the linear form
        linearForm(i) = A*v;
    end
end

figure(1), clf
% Plot the linear form
plot(x, linearForm, 'LineWidth', 2)
title('Linear form of vector v = [x_1, x_2]')
xlabel('x'), ylabel('Value')
grid on


%%

% Bilinear Form
B = [1 2; 2 3]; % Example matrix for bilinear form
wi1 = -2:.1:2; % Range of weights for first dimension
wi2 = -3:.1:3; % Range of weights for second dimension

bilinearForm = zeros(length(wi1), length(wi2));
for i = 1:length(wi1)
    for j = 1:length(wi2)
        % Define the weights for this iteration
        w = [wi1(i); wi2(j)];
        
        % Compute the bilinear form of the matrix
        bilinearForm(i,j) = w'*B*w;
    end
end

figure(2), clf
% Create a rotatable image
surf(wi1, wi2, bilinearForm'), shading interp
title('Visual representation of bilinear form of matrix B')
xlabel('W1'), ylabel('W2'), zlabel('Value')
rotate3d on


%%

% Quadratic Form
C = [1 2; 2 9]; % Example matrix for quadratic form
wi = -2:.1:2; % Range of weights

quadraticForm = zeros(length(wi));
for i = 1:length(wi)
    for j = 1:length(wi)
        % Define the weights for this iteration
        w = [wi(i); wi(j)];
        
        normfact = w'*w;

        % Compute the quadratic form of the matrix
        quadraticForm(i,j) = w'*C*w / normfact;
    end
end

figure(3), clf
% Create a rotatable image
surf(wi, wi, quadraticForm'), shading interp
title('Visual representation of quadratic form of matrix C')
xlabel('W1'), ylabel('W2'), zlabel('Value')
rotate3d on

[eigvecs,eigvals] = eig(C);
hold on
plot3([0 eigvecs(1,1)],[0 eigvecs(2,1)],[1 1]*max(quadraticForm(:)),'w','linew',3)
plot3([0 eigvecs(1,2)],[0 eigvecs(2,2)],[1 1]*max(quadraticForm(:)),'m','linew',3)


%% 

C = [1 2; 2 9]; % Example matrix for quadratic form
wi = -2:0.1:2; % Range of weights

magnitudes = zeros(1, length(wi)^2);
quadraticForm = zeros(1, length(wi)^2);
index = 1;

for i = 1:length(wi)
    for j = 1:length(wi)
        % Define the weights for this iteration
        w = [wi(i); wi(j)];
        
        normfact = w'*w;
        magnitudes(index) = normfact;
       
        % Compute the quadratic form of the matrix
        quadraticForm(index) = w'*C*w;
        
        index = index + 1;
    end
end

figure(4), clf
% Plot the quadratic form against magnitudes
plot(magnitudes, quadraticForm)
title('Visual representation of quadratic form of matrix C')
xlabel('Magnitude of weight vector'), ylabel('Quadratic form')
