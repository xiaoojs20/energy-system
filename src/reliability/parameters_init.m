% clc;clear;
% BESS parameter
num_cell=36; % cells/module
num_module=14; % modules/string
num_string=9; % strings/array
num_array=10; % arrays/system

num_conv=10;
num_fuse_in_conv=20;
num_fuse_out_conv=20;
num_fuse_in_inv=20;
num_cb=10;
num_inv=10;

% number of failures for a year
lambda_bm=0.0312;
mu_bm=10;
lambda_conv=0.125;
mu_conv=26;
lambda_inv=0.143;
mu_inv=21;
lambda_fuse=0.05;
mu_fuse=52;
lambda_cb=0.1;
mu_cb=10;
lambda_relay=0.1;
mu_relay=10;
lambda_diode=0.1;
mu_diode=26;
lambda_cap=0.4;
mu_cap=26;
lambda_inductor=0.4;
mu_inductor=26;
lambda_IGBT=0.3;
mu_IGBT=17;

% reliability
a_bm=mu_bm/(lambda_bm+mu_bm);
a_conv=mu_conv/(lambda_conv+mu_conv);
a_inv=mu_inv/(lambda_inv+mu_inv);
a_fuse=mu_fuse/(lambda_fuse+mu_fuse);
a_cb=mu_cb/(lambda_cb+mu_cb);
a_relay=mu_relay/(lambda_relay+mu_relay); 
a_diode=mu_diode/(lambda_diode+mu_diode);
a_cap=mu_cap/(lambda_cap+mu_cap);
a_inductor=mu_inductor/(lambda_inductor+mu_inductor);

% 能量冗余度
re=0.9;
lowerbound_string=num_array*num_string*re;

%% PB-BESS
% BESS
lambda_string=num_module*lambda_bm;
mu_string=(lambda_string*(mu_bm^num_module))/((mu_bm^num_module)*(num_module*lambda_bm/mu_bm));
a_string=mu_string/(lambda_string+mu_string);
% lambda_BESS=num_array*num_string*lambda_string;
% PI_BESS=(mu_string^(num_array*num_string));
% mu_BESS=(lambda_BESS*PI_BESS)/(PI_BESS*(num_array*num_string*lambda_string/mu_string));
% DC-DC
lambda_DCDC=num_array*lambda_conv+num_array*lambda_fuse+num_array*lambda_fuse;
PI_DCDC=(mu_conv^num_array)*(mu_fuse^num_array)*(mu_fuse^num_array);
mu_DCDC=(lambda_DCDC*PI_DCDC)/(PI_DCDC*(num_array*lambda_conv/mu_conv+2*num_array*lambda_fuse/mu_fuse));
% DC-AC
lambda_ACDC=num_inv*lambda_cb+num_inv*lambda_fuse+num_inv*lambda_inv;
PI_ACDC=(mu_cb^num_inv)*(mu_fuse^num_inv)*(mu_inv^num_inv);
mu_ACDC=(lambda_ACDC*PI_ACDC)/(PI_ACDC*(num_inv*lambda_cb/mu_cb+num_inv*lambda_fuse/mu_fuse+num_inv*lambda_inv/mu_inv));
% filter
lambda_filter=1.87e-7*8760;
mu_filter=mu_DCDC+mu_ACDC;





