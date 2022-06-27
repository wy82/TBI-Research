function strainintensity(Ns,Nc,Nd,name)
    % Setup
    a = arduino;
    configurePin(a,'D10','DigitalOutput');
    configurePin(a,'A0','AnalogInput');
    si = zeros(Ns,Nc,Nd);
    writeDigitalPin(a,'D10',true);
    x = 0.2:0.2:20;
    % LED
    i = 1;
    j = 1;
    k = 1;
    period = 0.2;
    while i <= Ns
        disp(append('Sensor #',int2str(i)));
        while j <= Nc
            h = animatedline;
            axis([0 20 0 5]);
            input(append('Cycle #',int2str(j),': '));
            pause(0.1)
            t0 = tic;
            while k <= Nd
                delta = period*k - toc(t0);
                toc(t0)
                if delta > 0
                    pause(delta);
                end
                disp(append('Displacement #',int2str(k),': '));
                % Record intensity
                si(i,j,k) = readVoltage(a,'A0');
                disp(si(i,j,k))
                addpoints(h,x(k),si(i,j,k))
                k = k + 1;
            end
            close all;

            k = 1;
            j = j + 1;
        end
        i = i + 1;
        j = 1;
        txt = input('','s');
        if txt == 'r'
            i = i - 1;
            continue;
        end
        save(name,'si');
    end
    save(name,'si');
    clear a;
end