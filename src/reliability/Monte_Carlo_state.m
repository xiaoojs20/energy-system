% Monte Carlo state
% string failure

%% PB-BESS
% 一个BM故障，则string故障
MC_number=10000;
string_state=zeros(num_array*num_string,MC_number);
PB_BESS_state=zeros(1,MC_number);
for j=1:MC_number
    for i=1:num_array*num_string
        if rand <= a_string % 没有故障的话
            string_state(i,j)=1;
        end
    end
    if nnz(string_state(:,j))>num_array*num_string*re
        PB_BESS_state(1,j)=1;
    end
end
a_BESS=nnz(PB_BESS_state)/MC_number;
a_DCDC=mu_DCDC/(lambda_DCDC+mu_DCDC);
a_ACDC=mu_ACDC/(lambda_ACDC+mu_ACDC);
a_filter=mu_filter/(lambda_filter+mu_filter);

a_PB_system=a_BESS*a_DCDC*a_ACDC*a_filter

%% IPB-BESS
% 考虑使用IGBT切断故障BM
lambda_switch=lambda_IGBT+lambda_diode;
mu_switch=(lambda_switch*mu_IGBT*mu_diode)/(mu_IGBT*mu_diode*((lambda_IGBT/mu_IGBT)+(lambda_diode/mu_diode)));
a_switch=mu_switch/(lambda_switch+mu_switch);

lambda_parallel=(lambda_IGBT+lambda_bm)*num_string;
PI_parallel=mu_IGBT^num_string*mu_diode^num_string;
mu_parallel=(lambda_parallel*PI_parallel)/(PI_parallel*((num_string*lambda_IGBT/mu_IGBT)+(num_string*lambda_bm/mu_bm)));
a_parallel=mu_parallel/(lambda_parallel+mu_parallel)

lambda_series=(lambda_parallel+lambda_IGBT)*num_module;
PI_series=mu_parallel^num_module*mu_IGBT^num_module;
mu_series=(lambda_series*PI_series)/(PI_series*((num_module*lambda_parallel/mu_parallel)+(num_module*lambda_IGBT/mu_IGBT)));
a_series=mu_series/(lambda_series+mu_series)

for j=1:MC_number
    for i=1:num_array*num_string
        if rand <= a_string % 没有故障的话
            string_state(i,j)=1;
        end
    end
    if nnz(string_state(:,j))>num_array*num_string*re
        PB_BESS_state(1,j)=1;
    end
end

