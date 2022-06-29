function curvatureintensity(Ns,Nd,name)
    % Setup
    a = arduino;
    configurePin(a,'D10','DigitalOutput');
    configurePin(a,'A0','AnalogInput');
    cui = zeros(Ns,Nd);
    writeDigitalPin(a,'D10',true);
    % LED
    i = 1;
    j = 1;
    while i <= Ns
        disp(append('Sensor #',int2str(i)));
        while j <= Nd
            input(append('Curvature #',int2str(j),': '));
            % Record intensity
            cui(i,j) = readVoltage(a,'A0');
            disp(cui(i,j))
            j = j + 1;
            txt = input("Press 'r' to redo: ",'s');
            if txt == 'r'
                j = j - 1;
                continue;
            end
        end
        j = 1;
        i = i + 1;
        save(name,'cui');
    end
    save(name,'cui');
    clear a;
end