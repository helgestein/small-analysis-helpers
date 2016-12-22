function bg = shirleyProcSher(y,iterations)
    y = flipud(y); %because our Kratos data needs to be flipped u/d
    len = length(y); %stopping criterion
    y = smooth(y,'sgolay',3); %smoothing the data
    a = y(1); %first element 
    b = y(end); %last element
    u = linspace(a,b,len).'; %initial guess for the background
    
    for k=1:iterations
         for i = 1:len-1
             p = trapz(y(1:i)-u(1:i)); %integrate left side
             q = trapz(y(i:end)-u(i:end)); %integrate right side
             u(i) = (a-b)*q/(p+q)+b; %calculate background iteration
         end
     end
     bg = flipud(u); %return data flipped
end