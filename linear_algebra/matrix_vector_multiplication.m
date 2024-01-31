% Vector Addition Visualization

% Define vectors
v1 = [2; 3];   % Example vector 1
v2 = [1; -2];  % Example vector 2

% Perform vector addition
v_result = v1 + v2;

% Plotting
figure;
hold on;

% Plot vector 1
quiver(0, 0, v1(1), v1(2), 0, 'b', 'LineWidth', 2, 'MaxHeadSize', 0.5);
text(v1(1)/2, v1(2)/2, 'Vector 1', 'FontSize', 10, 'Color', 'b');

% Plot vector 2
quiver(v1(1), v1(2), v2(1), v2(2), 0, 'r', 'LineWidth', 2, 'MaxHeadSize', 0.5);
text((v1(1) + v1(1) + v2(1))/2, (v1(2) + v1(2) + v2(2))/2, 'Vector 2', 'FontSize', 10, 'Color', 'r');

% Plot the result vector
quiver(0, 0, v_result(1), v_result(2), 0, 'g', 'LineWidth', 2, 'MaxHeadSize', 0.5);
text(v_result(1)/2, v_result(2)/2, 'Resultant Vector', 'FontSize', 10, 'Color', 'g');

% Set axis limits and labels
axis equal;
xlim([-5, 5]);
ylim([-5, 5]);
xlabel('X-axis');
ylabel('Y-axis');
title('Vector Addition Visualization');

hold off;
