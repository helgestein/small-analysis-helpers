function scatterPie(pos, pieDist, colors)

%h=fill([0 1 1 0],[0 0 1 1],'white','linewidth',0);

%this scales everything between >0 to 1
x = (pos(:,1)-min(pos(:,1)))./max(pos(:,1)-min(pos(:,1)));
y = (pos(:,2)-min(pos(:,2)))./max(pos(:,2)-min(pos(:,2)));

%colors = [0,1,0; 1,0,0; 0,0,1; 0.5,0.5,1; 1,0,1];

hold on

for i=1:length(x)
    vec = [0, pieDist(i,:)];
    vec = vec./sum(vec)*360;
    %rewrite vec so that the plotting routine accepts it
    for k=2:length(vec)
        vec(k) = vec(k)+vec(k-1);
    end
    %plot piecharts
    for k=1:3
        %matlabs own function was not useful
        %so i wrote my own pie chart plotting function
        %without the clutter
        pieplo(vec(k),vec(k+1), [x(i),y(i)], 0.02, colors(k,:));
    end
end

hold off
axis image
axis off
htick = [];
end