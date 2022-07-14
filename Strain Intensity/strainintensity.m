function strainintensity(Ns,Nc,Nd,Nr,name)
    % Setup
    %{
    a = arduino;
    configurePin(a,'D10','DigitalOutput');
    configurePin(a,'A0','AnalogInput');
    %}
    si = zeros(Ns,Nc,Nd);
    %writeDigitalPin(a,'D10',true);
    x = linspace(0,Nr,Nd+1);
    x = x(2:end);
    sensors = 1:Ns;
    % LED
    i = 0;
    j = 1;
    k = 1;
    period = 0.2;
    while true
        txt = input('Next Sensor: ','s');
        if txt == 'q'
            break;
        end
        if txt ~= 'r' || i == 0
            i = str2double(txt);
            sensors = sensors(sensors ~= i);
        end
        disp(append('Sensor #',int2str(i)));
        while j <= Nc
            h = animatedline;
            axis([0 Nr 0 5]);
            input(append('Cycle #',int2str(j),': '));
            pause(0.16)
            t0 = tic;
            while k <= Nd
                delta = period*k - toc(t0);
                toc(t0)
                if delta > 0
                    pause(delta);
                end
                disp(append('Displacement #',int2str(k),': '));
                % Record intensity
                %si(i,j,k) = readVoltage(a,'A0');
                disp(si(i,j,k))
                addpoints(h,x(k),si(i,j,k))
                k = k + 1;
            end
            close all;
            k = 1;
            j = j + 1;
        end
        j = 1;
        save(name,'si');
    end
    save(name,'si');
    %clear a;
end