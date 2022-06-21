function strainintensity(Ns,Nd)
    % Setup
    a = arduino;
    configurePin(a,'D10','DigitalOutput');
    configurePin(a,'A0','AnalogInput');
    si = zeros(Ns,Nd);
    
    % LED
    i = 1;
    j = 1;
    while i <= Ns
        disp(append('Sensor #',int2str(i)));

        while j <= Nd
            d = input(append('Displacement #',int2str(j),': '),'s');
            % Record intensity
            writeDigitalPin(a,'D10',true);
            pause(0.1);
            si(i,j) = readVoltage(a,'A0')
            j = j + 1;
        end
        i = i + 1;
        j = 1;
        txt = input('','s');
        if txt == 'r'
            i = i - 1;
            continue;
        end
        save('si','si')
    end
    save('si','si');
    clear a;
end