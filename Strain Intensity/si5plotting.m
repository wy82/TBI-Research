load('si5.mat', 'si');
xaxis = 0.2:0.2:20;

specimen = 4;
runPerSpeci = 5;
col = ['r','k','b','m','c','g','y'];
line = ['.', '-', '-', '-', '-'];

for i = 1:specimen
    for j = 1:runPerSpeci
        voltage = reshape(si(i, j, :), [100, 1]);
        plot(xaxis, voltage, strcat(line(j),col(i)));
        hold on
    end
end
set(gca,'TickLabelInterpreter','latex');
xlabel('\% Strain','interpreter','latex');
ylabel('Voltage','interpreter','latex');
set(gca,'FontSize',15);

h = findobj('Marker','.');
leg = legend(h(1:4),{'1', '2', '12', '14'});
set(leg,'Interpreter','latex');
set(leg,'FontSize',15);

saveas(gcf,'si5','fig');
saveas(gcf,'si5','png');


