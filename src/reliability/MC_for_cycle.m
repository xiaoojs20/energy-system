clc;
num_bm=num_array*num_string*num_module;
% num_bm=10;

max_cycle=2000;
% (1260 bm, 2000 cycles)
battery_state=ones(num_bm,max_cycle);
% failure probability of battery for all cycles
wpdf_LFP=wblpdf(cycle,lambda_LFP,k_LFP); 
wcdf_LFP=wblcdf(cycle,lambda_LFP,k_LFP); 

battery_p_init=gen_fail(0,num_bm);
% Maintain an array of healthy battery numbers per cycle
bm_healthy=num_bm*ones(1,max_cycle); 

modified_p=battery_p_init; 
re=0.8;
BESS_state=1;
BESS_life=0;

for j=2:max_cycle
    fprintf(['cycle ' num2str(j) ' starts!!\n']);
    % modify the failure probability, if needed
    battery_p=gen_fail(num_bm-bm_healthy(j-1),num_bm);
    modified_p(j-1)=battery_p(j-1);
    for i=1:num_bm
        % If the battery had failed, we don't need to consider it
        if battery_state(i,j-1)==0 
            continue;
        end
        % If the battery is healthy, we test if it failed(set 0)
        if rand<=modified_p(j-1)
            battery_state(i,j:end)=0;
            fprintf(['battery ' num2str(i) ' failed!!\n']);
            bm_healthy(j)=bm_healthy(j)-1;
            bm_healthy(j+1:end)=bm_healthy(j);
        end
    end
    fprintf(['healthy battery num: ' num2str(bm_healthy(j)) ' !!\n']);

    if bm_healthy(j)/num_bm<re && BESS_state==1
        BESS_state=0;
        BESS_life=j;
    end

    % now we know the battery state in j cycle
    % we should modify the failure probability, if there are new bms failed.
    
end

fprintf(['BESS life ' num2str(BESS_life) ' cycles !!\n']);

cycle=1:max_cycle;

% figure;
% plot(cycle,bm_healthy,'LineWidth',2);
% hold on;
% plot(BESS_life,bm_healthy(BESS_life),'LineWidth',2,'Marker','o');
% grid on;
% xlabel('cycle','FontSize',12,'Interpreter','Latex');
% ylabel('number of healthy bm','FontSize',12,'Interpreter','Latex');
% legend('healthy bm', 'BESS life');
% title('Healthy bm per cycle and BESS life','FontSize',16,'Interpreter','Latex');
% set(gcf,'Units','inches','Position',[5 5 10 6])
% saveas(gcf,'../figures/Healthy bm per cycle and BESS life.png');

figure;
plot(cycle(1:end-1),abs(diff(bm_healthy))/num_bm,'LineWidth',2);
hold on;
plot(cycle,wpdf_LFP,'LineWidth',2);
grid on;
xlabel('cycle','FontSize',12,'Interpreter','Latex');
ylabel('number of failed bm','FontSize',12,'Interpreter','Latex');
legend('failed bm', 'Weibull');
title('failed bm vs Weibull','FontSize',16,'Interpreter','Latex');
set(gcf,'Units','inches','Position',[5 5 10 6])
% saveas(gcf,'../figures/failed bm vs Weibull.png');
% 
% figure;
% plot(cycle(1:end-1),battery_p_init,'LineWidth',2);
% hold on;
% plot(cycle(1:end-1),modified_p,'LineWidth',2);
% plot(cycle(1:end-1),battery_p,'LineWidth',2);
% grid on;
% xlabel('cycle','FontSize',12,'Interpreter','Latex');
% ylabel('probability','FontSize',12,'Interpreter','Latex');
% legend('origin', 'modified', 'final');
% title('comparison before and after correction of failure probability','FontSize',16,'Interpreter','Latex');
% set(gcf,'Units','inches','Position',[5 5 10 6])
% saveas(gcf,'../figures/comparison before and after correction of failure probability.png');
% 
% 
% figure;
% plot(1:BESS_life,battery_p_init(1:BESS_life),'LineWidth',2);
% hold on;
% plot(1:BESS_life,modified_p(1:BESS_life),'LineWidth',2);
% plot(1:BESS_life,battery_p(1:BESS_life),'LineWidth',2);
% grid on;
% xlabel('cycle','FontSize',12,'Interpreter','Latex');
% ylabel('probability','FontSize',12,'Interpreter','Latex');
% legend('origin', 'modified', 'final');
% title('comparison before and after correction of failure probability(till BESS failed)','FontSize',16,'Interpreter','Latex');
% set(gcf,'Units','inches','Position',[5 5 10 6])
% saveas(gcf,'../figures/comparison before and after correction of failure probability(till BESS failed).png');
