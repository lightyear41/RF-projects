# -*- coding: utf-8 -*-

import empro.toolkit.adv as adv

def main():
	path=r"C:/Users/Public/MyWorkspace1_wrk"
	lib=r"MyLibrary1_lib"
	subst=r"MyLibrary1_lib/substrate1.subst"
	substlib=r"MyLibrary1_lib"
	substname=r"substrate1"
	cell=r"015um_MOSFET_For_Harmonics"
	view=r"layout"
	libS3D=r"simulation/MyLibrary1_lib/015um_%M%O%S%F%E%T_%For_%Harmonics/_3%D%Viewer/extra/0/proj_libS3D.xml"
	varDictionary={}
	exprDictionary={}
	adv.loadDesign(path=path, lib=lib, subst=subst, substlib=substlib, substname=substname, cell=cell, view=view, libS3D=libS3D, var_dict=varDictionary, expr_dict=exprDictionary)
