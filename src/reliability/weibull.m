%% Initialization
% clc;clear;

%% LFP
lambda_LFP=926.78; 
k_LFP=11.17; 
cycle=1:2000;

wpdf_LFP=wblpdf(cycle,lambda_LFP,k_LFP); 
wcdf_LFP=wblcdf(cycle,lambda_LFP,k_LFP); 
wrf_LFP=1-wcdf_LFP;
fail_LFP=(wpdf_LFP+1e-15)./wrf_LFP;
p_fail=diff(wcdf_LFP)./wrf_LFP(1:end-1);

dec=0.9;
wpdf_LFP_dec=wblpdf(cycle,lambda_LFP,k_LFP*dec); 
wcdf_LFP_dec=wblcdf(cycle,lambda_LFP*dec,k_LFP*dec); 
wrf_LFP_dec=1-wcdf_LFP_dec;
fail_LFP_dec=(wpdf_LFP_dec+1e-15)./wrf_LFP_dec;
p_fail_dec=diff(wcdf_LFP_dec)./wrf_LFP_dec(1:end-1);


figure;
plot(cycle,wpdf_LFP,'LineWidth',2);
hold on;
plot(cycle,wpdf_LFP_dec,'LineWidth',2);
grid on;
xlabel('cycle','FontSize',12,'Interpreter','Latex');
ylabel('probability','FontSize',12,'Interpreter','Latex');
legend(['k=' num2str(k_LFP) ' $\lambda=$' num2str(lambda_LFP)],['k=' num2str(k_LFP*dec) ' $\lambda$=' num2str(lambda_LFP*dec)],'Interpreter','Latex');
title('磷酸铁锂电池寿命分布','FontSize',16);
saveas(gcf,'../figures/磷酸铁锂电池寿命分布.png');

figure;
plot(cycle,wcdf_LFP,'LineWidth',2);
hold on;
plot(cycle,wcdf_LFP_dec,'LineWidth',2);
grid on;
xlabel('cycle','FontSize',12,'Interpreter','Latex');
ylabel('probability','FontSize',12,'Interpreter','Latex');
legend(['k=' num2str(k_LFP) ' $\lambda=$' num2str(lambda_LFP)],['k=' num2str(k_LFP*dec) ' $\lambda$=' num2str(lambda_LFP*dec)],'Interpreter','Latex');
title('磷酸铁锂电池寿命累计分布','FontSize',16);
saveas(gcf,'../figures/磷酸铁锂电池寿命累计分布.png');

figure;
plot(cycle(1:end-1),p_fail,'LineWidth',2);
hold on;
plot(cycle(1:end-1),p_fail_dec,'LineWidth',2);
grid on;
xlabel('cycle','FontSize',12,'Interpreter','Latex');
ylabel('probability','FontSize',12,'Interpreter','Latex');
legend(['k=' num2str(k_LFP) ' $\lambda=$' num2str(lambda_LFP)],['k=' num2str(k_LFP*dec) ' $\lambda$=' num2str(lambda_LFP*dec)],'Interpreter','Latex');
title('磷酸铁锂电池各循环故障概率','FontSize',16);
saveas(gcf,'../figures/磷酸铁锂电池各循环故障概率.png');

figure;
plot(cycle,fail_LFP,'LineWidth',2);
hold on;
plot(cycle,fail_LFP_dec,'LineWidth',2);
grid on;
xlabel('cycle','FontSize',12,'Interpreter','Latex');
ylabel('$\lambda$','FontSize',12,'Interpreter','Latex');
legend(['k=' num2str(k_LFP) ' $\lambda=$' num2str(lambda_LFP)],['k=' num2str(k_LFP*dec) ' $\lambda$=' num2str(lambda_LFP*dec)],'Interpreter','Latex');
title('磷酸铁锂电池故障率分布','FontSize',16);
saveas(gcf,'../figures/磷酸铁锂电池故障率分布.png');


