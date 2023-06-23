function p_fail=gen_fail(failednum, totalnum)
    lambda_LMO=926.78; 
    k_LFP=11.17; 
    cycle=1:2000;
    proportion_failed = failednum/totalnum;

%     wpdf_LFP=wblpdf(cycle,lambda_LMO,k_LFP); 
%     wcdf_LFP=wblcdf(cycle,lambda_LMO,k_LFP); 
%     wrf_LFP=1-wcdf_LFP;
%     fail_LFP=(wpdf_LFP+1e-15)./wrf_LFP;
    
    dec=1-0.1*proportion_failed;
    wpdf_LFP_dec=wblpdf(cycle,lambda_LMO*dec,k_LFP*dec); 
    wcdf_LFP_dec=wblcdf(cycle,lambda_LMO*dec,k_LFP*dec); 
    wrf_LFP_dec=1-wcdf_LFP_dec;
    fail_LFP_dec=(wpdf_LFP_dec+1e-15)./wrf_LFP_dec;

    p_fail=diff(wcdf_LFP_dec)./wrf_LFP_dec(1:end-1);
    [max_p,max_p_index]=max(p_fail(1:1150));
    p_fail(max_p_index:end)=max_p;
end