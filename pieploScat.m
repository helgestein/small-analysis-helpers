function [x,y] = pieploScat(startAngle, endAngle, center, radius ,color)
    %center 2D vec
    %radius = 1 ?
    %color 3tupel
    
    for j=1:floor(startAngle)
        p(j,:) = center;
    end
 
    for i = floor(startAngle):floor(endAngle)
        p(i+1,:) = radius*sin(i*pi/180) + center(1)
        p(i+1,:) = radius*cos(i*pi/180) + center(2);
    end
    center

    p(i+1,1) = center(1);
    p(i+1,2) = center(2);

    x = p(:,1);
    y = p(:,2);
    h=fill(x,y,color,'linewidth',1);

    axis off
    axis square
end