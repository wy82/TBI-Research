function maxvoltage(Ns)
    % Setup
    a = arduino;
    configurePin(a,'D10','DigitalOutput');
    configurePin(a,'A0','AnalogInput');
    vmax = zeros(1,Ns);
    
    % LED
    i = 1;
    while i <= Ns
        txt1 = input(append('Sensor #',int2str(i)),'s');
        writeDigitalPin(a,'D10',true);
        pause(0.1);
        vmax(i) = readVoltage(a,'A0')
        pause(0.1);
        txt2 = input('','s');
        % Redo
        if txt2 == 'r'
            continue;
        end
        i = i + 1;
    end
    %save('vmaxh','vmax');
    clear a;
end