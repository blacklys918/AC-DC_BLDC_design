print("HELLO!! Let's design your BLDC Moter.")
import math
A=input("If DC motor input 1  AC input 2")
A=int(A)
#馬達負載分析後需求的轉矩.轉速跟電壓
if A==1:
    print("you are design a DC BLDC motor")
    T_pk=float(input("input your Torque peak"))
    T_rated=float(input("input your Torque rated"))
    V=float(input("input your Voltage"))
    W_nl=float(input("input your no load Rotation speed in rad/s"))
    print()

#計算出電流峰值
    k_e=V/W_nl
    print("your k_e=",k_e)
    print()
    I_pk=T_pk/k_e
    print("your I_pk=",I_pk,"A")
    I_rated=T_rated/k_e
    print("your I_rated=",I_rated,"A")
    print()

#磁鐵參數
    print("let's talk about magnet")
    print()
    P_c=float(input("input magnet P_c"))
    g=float(input("input your airgap in mm"))
    C_phi=float(input("your C_phy"))
    print()
    l_m=P_c*g*C_phi
    print("your magnet length l_m=",l_m,"mm")
    print()
    K_l=float(input("input your k_l"))
    B_r=float(input("input your B_r"))
    K_r=float(input("input your K_r"))
    Mu_r=float(input("input your Mu_r"))
    B_g=(K_l*C_phi*B_r)/(1+K_r*(Mu_r/P_c))
    print()
    print("your B_g=",B_g,"T")
    print()

#輸入TRV 計算出Q值
    TRV=float(input("input your TRV"))
    sigma=TRV/2
    Q=sigma/B_g
    print()
    print("your Q=",Q,"A/mm")
    print()

#輸入馬達長度 計算出馬達半徑以及電流總值
    L=float(input("input your motor's Length in mm"))
    r_sqrt=T_rated/(TRV*3.14*L)
    R=r_sqrt**0.5
    R1=R*1000
    print("motor R=",R1,"mm")
    print()
    I_total=Q*3.14*2*R1
    print("your I_total=",I_total,"A")
    print()

#馬達槽極
    N_s=float(input("input motor's slot number"))
    N_m=float(input("input motor's pole number"))
    N_turns=(3/4)*Q*3.14*2*R1/(N_s*I_rated)
    N_turns=math.ceil(N_turns)
    print()
    print("number of turns per coil N_turns=",N_turns)
    print()

#計算槽面積
    I_slot=2*N_turns*I_rated
    print("your I_slot=",I_slot,"A")
    print()
    k_wb=float(input("input your k windings base in 0.XX"))
    k_wb=k_wb/100
    J=float(input("input your current density J in A/mm^2"))
    print()
    A_wb=I_rated/J
    R_wd_sqrt=A_wb/3.14
    R_wd=R_wd_sqrt**0.5
    print("your A windings base A_wb=",A_wb,"mm^2")
    print()
    A_slot=2*N_turns*I_rated/(J*k_wb)
    print("your A_slot=",A_slot,"mm^2")

#計算顎鐵厚度
    phi_total=B_g*3.14*2*R*L
    phi_loop=phi_total/N_m
    T_yoke=float(input("input your T_yoke"))
    print()
    W_yoke=phi_loop/(T_yoke*L)
    W_yoke=W_yoke*1000
    print("your yoke width W_yoke=",W_yoke,"mm")

elif A==2:
#馬達負載分析後需求的轉矩.轉速跟電壓
    print("you are design AC BLDC motor")
    T_pk=float(input("input your Torque peak"))
    T_rated=float(input("input your Torque rated"))
    V=float(input("input your Voltage"))
    W_nl=float(input("input your no load Rotation speed in rad/s"))
    print()

#電流改為rms值
    V_rms=V/(2**0.5)

#計算出電流峰值
    k_e=V_rms/W_nl
    print("your k_e=",k_e)
    print()
    k_t=k_e*(3**0.5)
    I_pk=T_pk/k_t
    print("your I_pk=",I_pk,"A")
    I_rated=T_rated/k_t
    print("your I_rated=",I_rated,"A")
    print()

#磁鐵參數
    print("let's talk about magnet")
    print()
    P_c=float(input("input magnet P_c"))
    g=float(input("input your airgap in mm"))
    C_phi=float(input("your C_phy"))
    print()
    l_m=P_c*g*C_phi
    print("your magnet length l_m=",l_m,"mm")
    print()
    K_l=float(input("input your k_l"))
    B_r=float(input("input your B_r"))
    K_r=float(input("input your K_r"))
    Mu_r=float(input("input your M_r"))
    B_g=(K_l*C_phi*B_r)/(1+K_r*(Mu_r/P_c))
    print()
    print("your B_g=",B_g,"T")
    print()

#輸入TRV 計算出Q值
    TRV=float(input("input your TRV"))
    sigma=TRV/2
    Q=sigma/B_g
    print()
    print("your Q=",Q,"A/mm")
    print()

#輸入馬達長度 計算出馬達半徑以及電流總值
    L=float(input("input your motor's Length in mm"))
    r_sqrt=T_rated/(TRV*3.14*L)
    R=r_sqrt**0.5
    R1=R*1000
    print("motor R=",R1,"mm")
    print()
    I_total=Q*3.14*2*R1
    print("your I_total=",I_total,"A")
    print()

#馬達槽極
    N_s=float(input("input motor's slot number"))
    N_m=float(input("input motor's pole number"))
    N_turns=(1/2)*Q*3.14*2*R1/(N_s*I_rated)
    N_turns=math.ceil(N_turns)
    print()
    print("number of turns per coil N_turns=",N_turns)
    print()

#計算槽面積
    I_slot=2*N_turns*I_rated
    print("your I_slot=",I_slot,"A")
    print()
    k_wb=float(input("input your k windings base in 0.XX"))
    k_wb=k_wb/100
    J=float(input("input your current density J in A/mm^2"))
    print()
    A_wb=I_rated/J
    R_wd_sqrt=A_wb/3.14
    R_wd=R_wd_sqrt**0.5
    print("your A windings base A_wb=",A_wb,"mm^2")
    print()
    A_slot=2*N_turns*I_rated/(J*k_wb)
    print("your A_slot=",A_slot,"mm^2")

#計算顎鐵厚度
    phi_total=B_g*3.14*2*R*L
    phi_loop=phi_total/N_m
    T_yoke=float(input("input your T_yoke"))
    print()
    W_yoke=phi_loop/(T_yoke*L)
    W_yoke=W_yoke*1000
    print("your yoke width W_yoke=",W_yoke,"mm")

else:
    print("ERROR you noob")
