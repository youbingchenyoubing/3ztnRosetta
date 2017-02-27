#coding=utf-8



def printResult(antibody_area,antigen_area,complex_area):
    print "antibody_area=",antibody_area
    print "antigen_area=",antigen_area
    print "complex_area=",complex_area
    print "the result area=",((antibody_area + antigen_area)-complex_area)

dot_solvent = 1
dot_density = 3
solvent_radius = 1.4
print "set parameters dot_solvent=%s,dot_density=%s" %(dot_solvent,dot_density)
#cmd.h_add()
#cmd.flag(25,"none")
cmd.set("dot_solvent",int(dot_solvent))
cmd.set("dot_density",int(dot_density))
cmd.set("solvent_radius",float(solvent_radius))
print "caculate 3ztn area"
antibody_area = cmd.get_area("antibody_3ztn")
antigen_area = cmd.get_area("antigen_3ztn")
complex_area = cmd.get_area("3ztn")
printResult(antibody_area,antigen_area,complex_area)
print "caculate 1ukf_epitobe_scaffold area"
antibody_area = cmd.get_area("antibody_epitobe_scaffold")
antigen_area = cmd.get_area("antigen_epitobe_scaffold")
complex_area = cmd.get_area("1ukf_epitobe_scaffold")
printResult(antibody_area,antigen_area,complex_area)


