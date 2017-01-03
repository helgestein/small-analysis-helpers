function [x,y] = pieplo(startAngle, endAngle, center, radius ,color)
    %center 2D vec
    %radius = 1 ?
    %color 3tupel
    
    for j=1:floor(startAngle)
        p(j,:) = center;
    end
 
    for i = floor(startAngle):floor(endAngle)
        p(i+1,:) = [radius*sin((i)*pi/180) , radius*cos(i*pi/180)] + center;
    end

    p(i+1,:) = center;

    x = p(:,1);
    y = p(:,2);
    h=fill(x,y,color,'linewidth',1);

    axis off
    axis square
end