#coding=utf-8
cmd.load("3ztn.pdb")
cmd.load("1ukf_epitobe_scaffold.pdb") #Rosetta Multigraft实验结果
cmd.select("antibody_3ztn","3ztn and (chain H or chain L)") #选出3ztn的抗体
cmd.select("antigen_3ztn","3ztn and not (chain H or chain L)")#将抗体从复合物剔除

cmd.select ("antibody_epitobe_scaffold","1ukf_epitobe_scaffold and (chain H or chain L)") #取出1ukf的抗体
cmd.select("antigen_epitobe_scaffold","1ukf_epitobe_scaffold and not (chain H or chain L)") #取出1ukf的epitobe-scaffold