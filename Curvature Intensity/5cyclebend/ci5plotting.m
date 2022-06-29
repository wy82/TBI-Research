load('ci53.mat', 'ci');
xaxis = 0.2:0.2:20;

specimen = 3;
runPerSpeci = 1;
col = ['r','k','b','m','c','g','y'];
line = ['-', '-', '-', '-', '-'];

for i = 1:specimen
    for j = 1:runPerSpeci
        voltage = reshape(ci(i, j, :), [100, 1]);
        plot(xaxis, voltage, strcat(line(j),col(i)));
        hold on
    end
end
set(gca,'TickLabelInterpreter','latex');
xlabel('\% Compression','interpreter','latex');
ylabel('Voltage','interpreter','latex');
set(gca,'FontSize',15);

h = findobj('Marker','.');
leg = legend(h(1:specimen),{'15','8','7'});
set(leg,'Interpreter','latex');
set(leg,'FontSize',15);

saveas(gcf,'ci53','fig');
saveas(gcf,'ci53','png');


