# -*- coding: utf-8 -*-
# atom_data.py
# Version 1.1
# A dictionary of meta data relating to the elements and their isotopes.
#
# Copyright (C) 2012-2015 Christian Hill
# Department of Physics and Astronomy, University College London
# christian.hill@ucl.ac.uk
# http://christianhill.co.uk/projects/pyvalem
#
# The support of the Atomic and Molecular Data Unit of the IAEA,
# the Data Center for Plasma Properties at the Korean National Fusion
# Research Institute and the Virtual Atomic and Molecular Data Centre
# during the development of this library is gratefully acknowledged.
#
# This file is part of PyValem
#
# PyValem is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyValem is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyValem.  If not, see <http://www.gnu.org/licenses/>
#
# The atom_data dictionary is keyed by element symbol and by the tuple
# (atomic_number, mass_number). Where mass_number=0, this indicates the
# (weighted) average isotopic composition for an element. The values in
# this dictionary are (atomic number, atomic weight, mass number, symbol).

# A list of all element symbols recognised by PyValem
element_symbols = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf']

atom_data={
'H':(1,1.007940,0,'H'),
(1,0):(1,1.007940,0,'H'),
'He':(2,4.002602,0,'He'),
(2,0):(2,4.002602,0,'He'),
'Li':(3,6.941000,0,'Li'),
(3,0):(3,6.941000,0,'Li'),
'Be':(4,9.012182,0,'Be'),
(4,0):(4,9.012182,0,'Be'),
'B':(5,10.811000,0,'B'),
(5,0):(5,10.811000,0,'B'),
'C':(6,12.010700,0,'C'),
(6,0):(6,12.010700,0,'C'),
'N':(7,14.006700,0,'N'),
(7,0):(7,14.006700,0,'N'),
'O':(8,15.999400,0,'O'),
(8,0):(8,15.999400,0,'O'),
'F':(9,18.998403,0,'F'),
(9,0):(9,18.998403,0,'F'),
'Ne':(10,20.179700,0,'Ne'),
(10,0):(10,20.179700,0,'Ne'),
'Na':(11,22.989769,0,'Na'),
(11,0):(11,22.989769,0,'Na'),
'Mg':(12,24.305000,0,'Mg'),
(12,0):(12,24.305000,0,'Mg'),
'Al':(13,26.981539,0,'Al'),
(13,0):(13,26.981539,0,'Al'),
'Si':(14,28.085500,0,'Si'),
(14,0):(14,28.085500,0,'Si'),
'P':(15,30.973762,0,'P'),
(15,0):(15,30.973762,0,'P'),
'S':(16,32.065000,0,'S'),
(16,0):(16,32.065000,0,'S'),
'Cl':(17,35.453000,0,'Cl'),
(17,0):(17,35.453000,0,'Cl'),
'Ar':(18,39.948000,0,'Ar'),
(18,0):(18,39.948000,0,'Ar'),
'K':(19,39.098300,0,'K'),
(19,0):(19,39.098300,0,'K'),
'Ca':(20,40.078000,0,'Ca'),
(20,0):(20,40.078000,0,'Ca'),
'Sc':(21,44.955912,0,'Sc'),
(21,0):(21,44.955912,0,'Sc'),
'Ti':(22,47.867000,0,'Ti'),
(22,0):(22,47.867000,0,'Ti'),
'V':(23,50.941500,0,'V'),
(23,0):(23,50.941500,0,'V'),
'Cr':(24,51.996100,0,'Cr'),
(24,0):(24,51.996100,0,'Cr'),
'Mn':(25,54.938045,0,'Mn'),
(25,0):(25,54.938045,0,'Mn'),
'Fe':(26,55.845000,0,'Fe'),
(26,0):(26,55.845000,0,'Fe'),
'Co':(27,58.933195,0,'Co'),
(27,0):(27,58.933195,0,'Co'),
'Ni':(28,58.693400,0,'Ni'),
(28,0):(28,58.693400,0,'Ni'),
'Cu':(29,63.546000,0,'Cu'),
(29,0):(29,63.546000,0,'Cu'),
'Zn':(30,65.380000,0,'Zn'),
(30,0):(30,65.380000,0,'Zn'),
'Ga':(31,69.723000,0,'Ga'),
(31,0):(31,69.723000,0,'Ga'),
'Ge':(32,72.640000,0,'Ge'),
(32,0):(32,72.640000,0,'Ge'),
'As':(33,74.921600,0,'As'),
(33,0):(33,74.921600,0,'As'),
'Se':(34,78.960000,0,'Se'),
(34,0):(34,78.960000,0,'Se'),
'Br':(35,79.904000,0,'Br'),
(35,0):(35,79.904000,0,'Br'),
'Kr':(36,83.798000,0,'Kr'),
(36,0):(36,83.798000,0,'Kr'),
'Rb':(37,85.467800,0,'Rb'),
(37,0):(37,85.467800,0,'Rb'),
'Sr':(38,87.620000,0,'Sr'),
(38,0):(38,87.620000,0,'Sr'),
'Y':(39,88.905850,0,'Y'),
(39,0):(39,88.905850,0,'Y'),
'Zr':(40,91.224000,0,'Zr'),
(40,0):(40,91.224000,0,'Zr'),
'Nb':(41,92.906380,0,'Nb'),
(41,0):(41,92.906380,0,'Nb'),
'Mo':(42,95.960000,0,'Mo'),
(42,0):(42,95.960000,0,'Mo'),
'Tc':(43,98.000000,0,'Tc'),
(43,0):(43,98.000000,0,'Tc'),
'Ru':(44,101.070000,0,'Ru'),
(44,0):(44,101.070000,0,'Ru'),
'Rh':(45,102.905500,0,'Rh'),
(45,0):(45,102.905500,0,'Rh'),
'Pd':(46,106.420000,0,'Pd'),
(46,0):(46,106.420000,0,'Pd'),
'Ag':(47,107.868200,0,'Ag'),
(47,0):(47,107.868200,0,'Ag'),
'Cd':(48,112.411000,0,'Cd'),
(48,0):(48,112.411000,0,'Cd'),
'In':(49,114.818000,0,'In'),
(49,0):(49,114.818000,0,'In'),
'Sn':(50,118.710000,0,'Sn'),
(50,0):(50,118.710000,0,'Sn'),
'Sb':(51,121.760000,0,'Sb'),
(51,0):(51,121.760000,0,'Sb'),
'Te':(52,127.600000,0,'Te'),
(52,0):(52,127.600000,0,'Te'),
'I':(53,126.904470,0,'I'),
(53,0):(53,126.904470,0,'I'),
'Xe':(54,131.293000,0,'Xe'),
(54,0):(54,131.293000,0,'Xe'),
'Cs':(55,132.905452,0,'Cs'),
(55,0):(55,132.905452,0,'Cs'),
'Ba':(56,137.327000,0,'Ba'),
(56,0):(56,137.327000,0,'Ba'),
'La':(57,138.905470,0,'La'),
(57,0):(57,138.905470,0,'La'),
'Ce':(58,140.116000,0,'Ce'),
(58,0):(58,140.116000,0,'Ce'),
'Pr':(59,140.907650,0,'Pr'),
(59,0):(59,140.907650,0,'Pr'),
'Nd':(60,144.242000,0,'Nd'),
(60,0):(60,144.242000,0,'Nd'),
'Pm':(61,145.000000,0,'Pm'),
(61,0):(61,145.000000,0,'Pm'),
'Sm':(62,150.360000,0,'Sm'),
(62,0):(62,150.360000,0,'Sm'),
'Eu':(63,151.964000,0,'Eu'),
(63,0):(63,151.964000,0,'Eu'),
'Gd':(64,157.250000,0,'Gd'),
(64,0):(64,157.250000,0,'Gd'),
'Tb':(65,158.925350,0,'Tb'),
(65,0):(65,158.925350,0,'Tb'),
'Dy':(66,162.500000,0,'Dy'),
(66,0):(66,162.500000,0,'Dy'),
'Ho':(67,164.930320,0,'Ho'),
(67,0):(67,164.930320,0,'Ho'),
'Er':(68,167.259000,0,'Er'),
(68,0):(68,167.259000,0,'Er'),
'Tm':(69,168.934210,0,'Tm'),
(69,0):(69,168.934210,0,'Tm'),
'Yb':(70,173.054000,0,'Yb'),
(70,0):(70,173.054000,0,'Yb'),
'Lu':(71,174.966800,0,'Lu'),
(71,0):(71,174.966800,0,'Lu'),
'Hf':(72,178.490000,0,'Hf'),
(72,0):(72,178.490000,0,'Hf'),
'Ta':(73,180.947880,0,'Ta'),
(73,0):(73,180.947880,0,'Ta'),
'W':(74,183.840000,0,'W'),
(74,0):(74,183.840000,0,'W'),
'Re':(75,186.207000,0,'Re'),
(75,0):(75,186.207000,0,'Re'),
'Os':(76,190.230000,0,'Os'),
(76,0):(76,190.230000,0,'Os'),
'Ir':(77,192.217000,0,'Ir'),
(77,0):(77,192.217000,0,'Ir'),
'Pt':(78,195.084000,0,'Pt'),
(78,0):(78,195.084000,0,'Pt'),
'Au':(79,196.966569,0,'Au'),
(79,0):(79,196.966569,0,'Au'),
'Hg':(80,200.590000,0,'Hg'),
(80,0):(80,200.590000,0,'Hg'),
'Tl':(81,204.383300,0,'Tl'),
(81,0):(81,204.383300,0,'Tl'),
'Pb':(82,207.200000,0,'Pb'),
(82,0):(82,207.200000,0,'Pb'),
'Bi':(83,208.980400,0,'Bi'),
(83,0):(83,208.980400,0,'Bi'),
'Po':(84,209.000000,0,'Po'),
(84,0):(84,209.000000,0,'Po'),
'At':(85,210.000000,0,'At'),
(85,0):(85,210.000000,0,'At'),
'Rn':(86,222.000000,0,'Rn'),
(86,0):(86,222.000000,0,'Rn'),
'Fr':(87,223.000000,0,'Fr'),
(87,0):(87,223.000000,0,'Fr'),
'Ra':(88,226.000000,0,'Ra'),
(88,0):(88,226.000000,0,'Ra'),
'Ac':(89,227.000000,0,'Ac'),
(89,0):(89,227.000000,0,'Ac'),
'Th':(90,232.038060,0,'Th'),
(90,0):(90,232.038060,0,'Th'),
'Pa':(91,231.035880,0,'Pa'),
(91,0):(91,231.035880,0,'Pa'),
'U':(92,238.028910,0,'U'),
(92,0):(92,238.028910,0,'U'),
'Np':(93,237.000000,0,'Np'),
(93,0):(93,237.000000,0,'Np'),
'Pu':(94,244.000000,0,'Pu'),
(94,0):(94,244.000000,0,'Pu'),
'Am':(95,243.000000,0,'Am'),
(95,0):(95,243.000000,0,'Am'),
'Cm':(96,247.000000,0,'Cm'),
(96,0):(96,247.000000,0,'Cm'),
'Bk':(97,247.000000,0,'Bk'),
(97,0):(97,247.000000,0,'Bk'),
'Cf':(98,251.000000,0,'Cf'),
(98,0):(98,251.000000,0,'Cf'),
'Es':(99,252.000000,0,'Es'),
(99,0):(99,252.000000,0,'Es'),
'Fm':(100,257.000000,0,'Fm'),
(100,0):(100,257.000000,0,'Fm'),
'Md':(101,258.000000,0,'Md'),
(101,0):(101,258.000000,0,'Md'),
'No':(102,259.000000,0,'No'),
(102,0):(102,259.000000,0,'No'),
'Lr':(103,262.000000,0,'Lr'),
(103,0):(103,262.000000,0,'Lr'),
'Rf':(104,265.000000,0,'Rf'),
(104,0):(104,265.000000,0,'Rf'),
'1H':(1,1.007825,1,'1H'),
(1,1):(1,1.007825,1,'1H'),
'2H':(1,2.014102,2,'2H'),
(1,2):(1,2.014102,2,'2H'),
'3H':(1,3.0160492,3,'3H'),
(1,3):(1,3.0160492,3,'3H'),
'3He':(2,3.016029,3,'3He'),
(2,3):(2,3.016029,3,'3He'),
'4He':(2,4.002603,4,'4He'),
(2,4):(2,4.002603,4,'4He'),
'6Li':(3,6.015123,6,'6Li'),
(3,6):(3,6.015123,6,'6Li'),
'7Li':(3,7.016005,7,'7Li'),
(3,7):(3,7.016005,7,'7Li'),
'9Be':(4,9.012182,9,'9Be'),
(4,9):(4,9.012182,9,'9Be'),
'10B':(5,10.012937,10,'10B'),
(5,10):(5,10.012937,10,'10B'),
'11B':(5,11.009305,11,'11B'),
(5,11):(5,11.009305,11,'11B'),
'12C':(6,12.000000,12,'12C'),
(6,12):(6,12.000000,12,'12C'),
'13C':(6,13.003355,13,'13C'),
(6,13):(6,13.003355,13,'13C'),
'14C':(6,14.003241989,14,'14C'),
(6,14):(6,14.003241989,14,'14C'),
'14N':(7,14.003074,14,'14N'),
(7,14):(7,14.003074,14,'14N'),
'15N':(7,15.000109,15,'15N'),
(7,15):(7,15.000109,15,'15N'),
'16O':(8,15.994915,16,'16O'),
(8,16):(8,15.994915,16,'16O'),
'17O':(8,16.999132,17,'17O'),
(8,17):(8,16.999132,17,'17O'),
'18O':(8,17.999161,18,'18O'),
(8,18):(8,17.999161,18,'18O'),
'19F':(9,18.998403,19,'19F'),
(9,19):(9,18.998403,19,'19F'),
'20Ne':(10,19.992440,20,'20Ne'),
(10,20):(10,19.992440,20,'20Ne'),
'21Ne':(10,20.993847,21,'21Ne'),
(10,21):(10,20.993847,21,'21Ne'),
'22Ne':(10,21.991385,22,'22Ne'),
(10,22):(10,21.991385,22,'22Ne'),
'23Na':(11,22.989769,23,'23Na'),
(11,23):(11,22.989769,23,'23Na'),
'24Mg':(12,23.985042,24,'24Mg'),
(12,24):(12,23.985042,24,'24Mg'),
'25Mg':(12,24.985837,25,'25Mg'),
(12,25):(12,24.985837,25,'25Mg'),
'26Mg':(12,25.982593,26,'26Mg'),
(12,26):(12,25.982593,26,'26Mg'),
'27Al':(13,26.981539,27,'27Al'),
(13,27):(13,26.981539,27,'27Al'),
'28Si':(14,27.976927,28,'28Si'),
(14,28):(14,27.976927,28,'28Si'),
'29Si':(14,28.976495,29,'29Si'),
(14,29):(14,28.976495,29,'29Si'),
'30Si':(14,29.973770,30,'30Si'),
(14,30):(14,29.973770,30,'30Si'),
'31P':(15,30.973762,31,'31P'),
(15,31):(15,30.973762,31,'31P'),
'32S':(16,31.972071,32,'32S'),
(16,32):(16,31.972071,32,'32S'),
'33S':(16,32.971459,33,'33S'),
(16,33):(16,32.971459,33,'33S'),
'34S':(16,33.967867,34,'34S'),
(16,34):(16,33.967867,34,'34S'),
'36S':(16,35.967081,36,'36S'),
(16,36):(16,35.967081,36,'36S'),
'35Cl':(17,34.968853,35,'35Cl'),
(17,35):(17,34.968853,35,'35Cl'),
'37Cl':(17,36.965903,37,'37Cl'),
(17,37):(17,36.965903,37,'37Cl'),
'36Ar':(18,35.967545,36,'36Ar'),
(18,36):(18,35.967545,36,'36Ar'),
'38Ar':(18,37.962732,38,'38Ar'),
(18,38):(18,37.962732,38,'38Ar'),
'40Ar':(18,39.962383,40,'40Ar'),
(18,40):(18,39.962383,40,'40Ar'),
'39K':(19,38.963707,39,'39K'),
(19,39):(19,38.963707,39,'39K'),
'40K':(19,39.963998,40,'40K'),
(19,40):(19,39.963998,40,'40K'),
'41K':(19,40.961826,41,'41K'),
(19,41):(19,40.961826,41,'41K'),
'40Ca':(20,39.962591,40,'40Ca'),
(20,40):(20,39.962591,40,'40Ca'),
'42Ca':(20,41.958618,42,'42Ca'),
(20,42):(20,41.958618,42,'42Ca'),
'43Ca':(20,42.958767,43,'43Ca'),
(20,43):(20,42.958767,43,'43Ca'),
'44Ca':(20,43.955482,44,'44Ca'),
(20,44):(20,43.955482,44,'44Ca'),
'46Ca':(20,45.953693,46,'46Ca'),
(20,46):(20,45.953693,46,'46Ca'),
'48Ca':(20,47.952534,48,'48Ca'),
(20,48):(20,47.952534,48,'48Ca'),
'45Sc':(21,44.955912,45,'45Sc'),
(21,45):(21,44.955912,45,'45Sc'),
'46Ti':(22,45.952632,46,'46Ti'),
(22,46):(22,45.952632,46,'46Ti'),
'47Ti':(22,46.951763,47,'47Ti'),
(22,47):(22,46.951763,47,'47Ti'),
'48Ti':(22,47.947946,48,'48Ti'),
(22,48):(22,47.947946,48,'48Ti'),
'49Ti':(22,48.947870,49,'49Ti'),
(22,49):(22,48.947870,49,'49Ti'),
'50Ti':(22,49.944791,50,'50Ti'),
(22,50):(22,49.944791,50,'50Ti'),
'50V':(23,49.947159,50,'50V'),
(23,50):(23,49.947159,50,'50V'),
'51V':(23,50.943959,51,'51V'),
(23,51):(23,50.943959,51,'51V'),
'50Cr':(24,49.946044,50,'50Cr'),
(24,50):(24,49.946044,50,'50Cr'),
'52Cr':(24,51.940508,52,'52Cr'),
(24,52):(24,51.940508,52,'52Cr'),
'53Cr':(24,52.940649,53,'53Cr'),
(24,53):(24,52.940649,53,'53Cr'),
'54Cr':(24,53.938880,54,'54Cr'),
(24,54):(24,53.938880,54,'54Cr'),
'55Mn':(25,54.938045,55,'55Mn'),
(25,55):(25,54.938045,55,'55Mn'),
'54Fe':(26,53.939611,54,'54Fe'),
(26,54):(26,53.939611,54,'54Fe'),
'56Fe':(26,55.934937,56,'56Fe'),
(26,56):(26,55.934937,56,'56Fe'),
'57Fe':(26,56.935394,57,'57Fe'),
(26,57):(26,56.935394,57,'57Fe'),
'58Fe':(26,57.933276,58,'58Fe'),
(26,58):(26,57.933276,58,'58Fe'),
'59Co':(27,58.933195,59,'59Co'),
(27,59):(27,58.933195,59,'59Co'),
'58Ni':(28,57.935343,58,'58Ni'),
(28,58):(28,57.935343,58,'58Ni'),
'60Ni':(28,59.930786,60,'60Ni'),
(28,60):(28,59.930786,60,'60Ni'),
'61Ni':(28,60.931056,61,'61Ni'),
(28,61):(28,60.931056,61,'61Ni'),
'62Ni':(28,61.928345,62,'62Ni'),
(28,62):(28,61.928345,62,'62Ni'),
'64Ni':(28,63.927966,64,'64Ni'),
(28,64):(28,63.927966,64,'64Ni'),
'63Cu':(29,62.929597,63,'63Cu'),
(29,63):(29,62.929597,63,'63Cu'),
'65Cu':(29,64.927790,65,'65Cu'),
(29,65):(29,64.927790,65,'65Cu'),
'64Zn':(30,63.929142,64,'64Zn'),
(30,64):(30,63.929142,64,'64Zn'),
'66Zn':(30,65.926033,66,'66Zn'),
(30,66):(30,65.926033,66,'66Zn'),
'67Zn':(30,66.927127,67,'67Zn'),
(30,67):(30,66.927127,67,'67Zn'),
'68Zn':(30,67.924844,68,'68Zn'),
(30,68):(30,67.924844,68,'68Zn'),
'70Zn':(30,69.925319,70,'70Zn'),
(30,70):(30,69.925319,70,'70Zn'),
'69Ga':(31,68.925574,69,'69Ga'),
(31,69):(31,68.925574,69,'69Ga'),
'71Ga':(31,70.924701,71,'71Ga'),
(31,71):(31,70.924701,71,'71Ga'),
'70Ge':(32,69.924247,70,'70Ge'),
(32,70):(32,69.924247,70,'70Ge'),
'72Ge':(32,71.922076,72,'72Ge'),
(32,72):(32,71.922076,72,'72Ge'),
'73Ge':(32,72.923459,73,'73Ge'),
(32,73):(32,72.923459,73,'73Ge'),
'74Ge':(32,73.921178,74,'74Ge'),
(32,74):(32,73.921178,74,'74Ge'),
'76Ge':(32,75.921403,76,'76Ge'),
(32,76):(32,75.921403,76,'76Ge'),
'75As':(33,74.921597,75,'75As'),
(33,75):(33,74.921597,75,'75As'),
'74Se':(34,73.922476,74,'74Se'),
(34,74):(34,73.922476,74,'74Se'),
'76Se':(34,75.919214,76,'76Se'),
(34,76):(34,75.919214,76,'76Se'),
'77Se':(34,76.919914,77,'77Se'),
(34,77):(34,76.919914,77,'77Se'),
'78Se':(34,77.917309,78,'78Se'),
(34,78):(34,77.917309,78,'78Se'),
'80Se':(34,79.916521,80,'80Se'),
(34,80):(34,79.916521,80,'80Se'),
'82Se':(34,81.916699,82,'82Se'),
(34,82):(34,81.916699,82,'82Se'),
'79Br':(35,78.918337,79,'79Br'),
(35,79):(35,78.918337,79,'79Br'),
'81Br':(35,80.916291,81,'81Br'),
(35,81):(35,80.916291,81,'81Br'),
'78Kr':(36,77.920365,78,'78Kr'),
(36,78):(36,77.920365,78,'78Kr'),
'80Kr':(36,79.916379,80,'80Kr'),
(36,80):(36,79.916379,80,'80Kr'),
'82Kr':(36,81.913484,82,'82Kr'),
(36,82):(36,81.913484,82,'82Kr'),
'83Kr':(36,82.914136,83,'83Kr'),
(36,83):(36,82.914136,83,'83Kr'),
'84Kr':(36,83.911507,84,'84Kr'),
(36,84):(36,83.911507,84,'84Kr'),
'86Kr':(36,85.910611,86,'86Kr'),
(36,86):(36,85.910611,86,'86Kr'),
'85Rb':(37,84.911790,85,'85Rb'),
(37,85):(37,84.911790,85,'85Rb'),
'87Rb':(37,86.909181,87,'87Rb'),
(37,87):(37,86.909181,87,'87Rb'),
'84Sr':(38,83.913425,84,'84Sr'),
(38,84):(38,83.913425,84,'84Sr'),
'86Sr':(38,85.909260,86,'86Sr'),
(38,86):(38,85.909260,86,'86Sr'),
'87Sr':(38,86.908877,87,'87Sr'),
(38,87):(38,86.908877,87,'87Sr'),
'88Sr':(38,87.905612,88,'88Sr'),
(38,88):(38,87.905612,88,'88Sr'),
'89Y':(39,88.905848,89,'89Y'),
(39,89):(39,88.905848,89,'89Y'),
'90Zr':(40,89.904704,90,'90Zr'),
(40,90):(40,89.904704,90,'90Zr'),
'91Zr':(40,90.905646,91,'91Zr'),
(40,91):(40,90.905646,91,'91Zr'),
'92Zr':(40,91.905041,92,'92Zr'),
(40,92):(40,91.905041,92,'92Zr'),
'94Zr':(40,93.906315,94,'94Zr'),
(40,94):(40,93.906315,94,'94Zr'),
'96Zr':(40,95.908273,96,'96Zr'),
(40,96):(40,95.908273,96,'96Zr'),
'93Nb':(41,92.906378,93,'93Nb'),
(41,93):(41,92.906378,93,'93Nb'),
'92Mo':(42,91.906811,92,'92Mo'),
(42,92):(42,91.906811,92,'92Mo'),
'94Mo':(42,93.905088,94,'94Mo'),
(42,94):(42,93.905088,94,'94Mo'),
'95Mo':(42,94.905842,95,'95Mo'),
(42,95):(42,94.905842,95,'95Mo'),
'96Mo':(42,95.904680,96,'96Mo'),
(42,96):(42,95.904680,96,'96Mo'),
'97Mo':(42,96.906021,97,'97Mo'),
(42,97):(42,96.906021,97,'97Mo'),
'98Mo':(42,97.905408,98,'98Mo'),
(42,98):(42,97.905408,98,'98Mo'),
'100Mo':(42,99.907477,100,'100Mo'),
(42,100):(42,99.907477,100,'100Mo'),
'96Ru':(44,95.907598,96,'96Ru'),
(44,96):(44,95.907598,96,'96Ru'),
'98Ru':(44,97.905287,98,'98Ru'),
(44,98):(44,97.905287,98,'98Ru'),
'99Ru':(44,98.905939,99,'99Ru'),
(44,99):(44,98.905939,99,'99Ru'),
'100Ru':(44,99.904219,100,'100Ru'),
(44,100):(44,99.904219,100,'100Ru'),
'101Ru':(44,100.905582,101,'101Ru'),
(44,101):(44,100.905582,101,'101Ru'),
'102Ru':(44,101.904349,102,'102Ru'),
(44,102):(44,101.904349,102,'102Ru'),
'104Ru':(44,103.905433,104,'104Ru'),
(44,104):(44,103.905433,104,'104Ru'),
'103Rh':(45,102.905504,103,'103Rh'),
(45,103):(45,102.905504,103,'103Rh'),
'102Pd':(46,101.905609,102,'102Pd'),
(46,102):(46,101.905609,102,'102Pd'),
'104Pd':(46,103.904036,104,'104Pd'),
(46,104):(46,103.904036,104,'104Pd'),
'105Pd':(46,104.905085,105,'105Pd'),
(46,105):(46,104.905085,105,'105Pd'),
'106Pd':(46,105.903486,106,'106Pd'),
(46,106):(46,105.903486,106,'106Pd'),
'108Pd':(46,107.903892,108,'108Pd'),
(46,108):(46,107.903892,108,'108Pd'),
'110Pd':(46,109.905153,110,'110Pd'),
(46,110):(46,109.905153,110,'110Pd'),
'107Ag':(47,106.905097,107,'107Ag'),
(47,107):(47,106.905097,107,'107Ag'),
'109Ag':(47,108.904752,109,'109Ag'),
(47,109):(47,108.904752,109,'109Ag'),
'106Cd':(48,105.906459,106,'106Cd'),
(48,106):(48,105.906459,106,'106Cd'),
'108Cd':(48,107.904184,108,'108Cd'),
(48,108):(48,107.904184,108,'108Cd'),
'110Cd':(48,109.903002,110,'110Cd'),
(48,110):(48,109.903002,110,'110Cd'),
'111Cd':(48,110.904178,111,'111Cd'),
(48,111):(48,110.904178,111,'111Cd'),
'112Cd':(48,111.902758,112,'112Cd'),
(48,112):(48,111.902758,112,'112Cd'),
'113Cd':(48,112.904402,113,'113Cd'),
(48,113):(48,112.904402,113,'113Cd'),
'114Cd':(48,113.903358,114,'114Cd'),
(48,114):(48,113.903358,114,'114Cd'),
'116Cd':(48,115.904756,116,'116Cd'),
(48,116):(48,115.904756,116,'116Cd'),
'113In':(49,112.904058,113,'113In'),
(49,113):(49,112.904058,113,'113In'),
'115In':(49,114.903878,115,'115In'),
(49,115):(49,114.903878,115,'115In'),
'112Sn':(50,111.904818,112,'112Sn'),
(50,112):(50,111.904818,112,'112Sn'),
'114Sn':(50,113.902779,114,'114Sn'),
(50,114):(50,113.902779,114,'114Sn'),
'115Sn':(50,114.903342,115,'115Sn'),
(50,115):(50,114.903342,115,'115Sn'),
'116Sn':(50,115.901741,116,'116Sn'),
(50,116):(50,115.901741,116,'116Sn'),
'117Sn':(50,116.902952,117,'117Sn'),
(50,117):(50,116.902952,117,'117Sn'),
'118Sn':(50,117.901603,118,'118Sn'),
(50,118):(50,117.901603,118,'118Sn'),
'119Sn':(50,118.903308,119,'119Sn'),
(50,119):(50,118.903308,119,'119Sn'),
'120Sn':(50,119.902195,120,'120Sn'),
(50,120):(50,119.902195,120,'120Sn'),
'122Sn':(50,121.903439,122,'122Sn'),
(50,122):(50,121.903439,122,'122Sn'),
'124Sn':(50,123.905274,124,'124Sn'),
(50,124):(50,123.905274,124,'124Sn'),
'121Sb':(51,120.903816,121,'121Sb'),
(51,121):(51,120.903816,121,'121Sb'),
'123Sb':(51,122.904214,123,'123Sb'),
(51,123):(51,122.904214,123,'123Sb'),
'120Te':(52,119.904020,120,'120Te'),
(52,120):(52,119.904020,120,'120Te'),
'122Te':(52,121.903044,122,'122Te'),
(52,122):(52,121.903044,122,'122Te'),
'123Te':(52,122.904270,123,'123Te'),
(52,123):(52,122.904270,123,'123Te'),
'124Te':(52,123.902818,124,'124Te'),
(52,124):(52,123.902818,124,'124Te'),
'125Te':(52,124.904431,125,'125Te'),
(52,125):(52,124.904431,125,'125Te'),
'126Te':(52,125.903312,126,'126Te'),
(52,126):(52,125.903312,126,'126Te'),
'128Te':(52,127.904463,128,'128Te'),
(52,128):(52,127.904463,128,'128Te'),
'130Te':(52,129.906224,130,'130Te'),
(52,130):(52,129.906224,130,'130Te'),
'127I':(53,126.904473,127,'127I'),
(53,127):(53,126.904473,127,'127I'),
'124Xe':(54,123.905893,124,'124Xe'),
(54,124):(54,123.905893,124,'124Xe'),
'126Xe':(54,125.904274,126,'126Xe'),
(54,126):(54,125.904274,126,'126Xe'),
'128Xe':(54,127.903531,128,'128Xe'),
(54,128):(54,127.903531,128,'128Xe'),
'129Xe':(54,128.904779,129,'129Xe'),
(54,129):(54,128.904779,129,'129Xe'),
'130Xe':(54,129.903508,130,'130Xe'),
(54,130):(54,129.903508,130,'130Xe'),
'131Xe':(54,130.905082,131,'131Xe'),
(54,131):(54,130.905082,131,'131Xe'),
'132Xe':(54,131.904154,132,'132Xe'),
(54,132):(54,131.904154,132,'132Xe'),
'134Xe':(54,133.905394,134,'134Xe'),
(54,134):(54,133.905394,134,'134Xe'),
'136Xe':(54,135.907219,136,'136Xe'),
(54,136):(54,135.907219,136,'136Xe'),
'133Cs':(55,132.905452,133,'133Cs'),
(55,133):(55,132.905452,133,'133Cs'),
'130Ba':(56,129.906321,130,'130Ba'),
(56,130):(56,129.906321,130,'130Ba'),
'132Ba':(56,131.905061,132,'132Ba'),
(56,132):(56,131.905061,132,'132Ba'),
'134Ba':(56,133.904508,134,'134Ba'),
(56,134):(56,133.904508,134,'134Ba'),
'135Ba':(56,134.905689,135,'135Ba'),
(56,135):(56,134.905689,135,'135Ba'),
'136Ba':(56,135.904576,136,'136Ba'),
(56,136):(56,135.904576,136,'136Ba'),
'137Ba':(56,136.905827,137,'137Ba'),
(56,137):(56,136.905827,137,'137Ba'),
'138Ba':(56,137.905247,138,'138Ba'),
(56,138):(56,137.905247,138,'138Ba'),
'138La':(57,137.907112,138,'138La'),
(57,138):(57,137.907112,138,'138La'),
'139La':(57,138.906353,139,'139La'),
(57,139):(57,138.906353,139,'139La'),
'136Ce':(58,135.907172,136,'136Ce'),
(58,136):(58,135.907172,136,'136Ce'),
'138Ce':(58,137.905991,138,'138Ce'),
(58,138):(58,137.905991,138,'138Ce'),
'140Ce':(58,139.905439,140,'140Ce'),
(58,140):(58,139.905439,140,'140Ce'),
'142Ce':(58,141.909244,142,'142Ce'),
(58,142):(58,141.909244,142,'142Ce'),
'141Pr':(59,140.907653,141,'141Pr'),
(59,141):(59,140.907653,141,'141Pr'),
'142Nd':(60,141.907723,142,'142Nd'),
(60,142):(60,141.907723,142,'142Nd'),
'143Nd':(60,142.909814,143,'143Nd'),
(60,143):(60,142.909814,143,'143Nd'),
'144Nd':(60,143.910087,144,'144Nd'),
(60,144):(60,143.910087,144,'144Nd'),
'145Nd':(60,144.912574,145,'145Nd'),
(60,145):(60,144.912574,145,'145Nd'),
'146Nd':(60,145.913117,146,'146Nd'),
(60,146):(60,145.913117,146,'146Nd'),
'148Nd':(60,147.916893,148,'148Nd'),
(60,148):(60,147.916893,148,'148Nd'),
'150Nd':(60,149.920891,150,'150Nd'),
(60,150):(60,149.920891,150,'150Nd'),
'144Sm':(62,143.911999,144,'144Sm'),
(62,144):(62,143.911999,144,'144Sm'),
'147Sm':(62,146.914898,147,'147Sm'),
(62,147):(62,146.914898,147,'147Sm'),
'148Sm':(62,147.914823,148,'148Sm'),
(62,148):(62,147.914823,148,'148Sm'),
'149Sm':(62,148.917185,149,'149Sm'),
(62,149):(62,148.917185,149,'149Sm'),
'150Sm':(62,149.917275,150,'150Sm'),
(62,150):(62,149.917275,150,'150Sm'),
'152Sm':(62,151.919732,152,'152Sm'),
(62,152):(62,151.919732,152,'152Sm'),
'154Sm':(62,153.922209,154,'154Sm'),
(62,154):(62,153.922209,154,'154Sm'),
'151Eu':(63,150.919850,151,'151Eu'),
(63,151):(63,150.919850,151,'151Eu'),
'153Eu':(63,152.921230,153,'153Eu'),
(63,153):(63,152.921230,153,'153Eu'),
'152Gd':(64,151.919791,152,'152Gd'),
(64,152):(64,151.919791,152,'152Gd'),
'154Gd':(64,153.920866,154,'154Gd'),
(64,154):(64,153.920866,154,'154Gd'),
'155Gd':(64,154.922622,155,'155Gd'),
(64,155):(64,154.922622,155,'155Gd'),
'156Gd':(64,155.922123,156,'156Gd'),
(64,156):(64,155.922123,156,'156Gd'),
'157Gd':(64,156.923960,157,'157Gd'),
(64,157):(64,156.923960,157,'157Gd'),
'158Gd':(64,157.924104,158,'158Gd'),
(64,158):(64,157.924104,158,'158Gd'),
'160Gd':(64,159.927054,160,'160Gd'),
(64,160):(64,159.927054,160,'160Gd'),
'159Tb':(65,158.925347,159,'159Tb'),
(65,159):(65,158.925347,159,'159Tb'),
'156Dy':(66,155.924283,156,'156Dy'),
(66,156):(66,155.924283,156,'156Dy'),
'158Dy':(66,157.924409,158,'158Dy'),
(66,158):(66,157.924409,158,'158Dy'),
'160Dy':(66,159.925197,160,'160Dy'),
(66,160):(66,159.925197,160,'160Dy'),
'161Dy':(66,160.926933,161,'161Dy'),
(66,161):(66,160.926933,161,'161Dy'),
'162Dy':(66,161.926798,162,'162Dy'),
(66,162):(66,161.926798,162,'162Dy'),
'163Dy':(66,162.928731,163,'163Dy'),
(66,163):(66,162.928731,163,'163Dy'),
'164Dy':(66,163.929175,164,'164Dy'),
(66,164):(66,163.929175,164,'164Dy'),
'165Ho':(67,164.930322,165,'165Ho'),
(67,165):(67,164.930322,165,'165Ho'),
'162Er':(68,161.928778,162,'162Er'),
(68,162):(68,161.928778,162,'162Er'),
'164Er':(68,163.929200,164,'164Er'),
(68,164):(68,163.929200,164,'164Er'),
'166Er':(68,165.930293,166,'166Er'),
(68,166):(68,165.930293,166,'166Er'),
'167Er':(68,166.932048,167,'167Er'),
(68,167):(68,166.932048,167,'167Er'),
'168Er':(68,167.932370,168,'168Er'),
(68,168):(68,167.932370,168,'168Er'),
'170Er':(68,169.935464,170,'170Er'),
(68,170):(68,169.935464,170,'170Er'),
'169Tm':(69,168.934213,169,'169Tm'),
(69,169):(69,168.934213,169,'169Tm'),
'168Yb':(70,167.933897,168,'168Yb'),
(70,168):(70,167.933897,168,'168Yb'),
'170Yb':(70,169.934762,170,'170Yb'),
(70,170):(70,169.934762,170,'170Yb'),
'171Yb':(70,170.936326,171,'171Yb'),
(70,171):(70,170.936326,171,'171Yb'),
'172Yb':(70,171.936382,172,'172Yb'),
(70,172):(70,171.936382,172,'172Yb'),
'173Yb':(70,172.938211,173,'173Yb'),
(70,173):(70,172.938211,173,'173Yb'),
'174Yb':(70,173.938862,174,'174Yb'),
(70,174):(70,173.938862,174,'174Yb'),
'176Yb':(70,175.942572,176,'176Yb'),
(70,176):(70,175.942572,176,'176Yb'),
'175Lu':(71,174.940772,175,'175Lu'),
(71,175):(71,174.940772,175,'175Lu'),
'176Lu':(71,175.942686,176,'176Lu'),
(71,176):(71,175.942686,176,'176Lu'),
'174Hf':(72,173.940046,174,'174Hf'),
(72,174):(72,173.940046,174,'174Hf'),
'176Hf':(72,175.941409,176,'176Hf'),
(72,176):(72,175.941409,176,'176Hf'),
'177Hf':(72,176.943221,177,'177Hf'),
(72,177):(72,176.943221,177,'177Hf'),
'178Hf':(72,177.943699,178,'178Hf'),
(72,178):(72,177.943699,178,'178Hf'),
'179Hf':(72,178.945816,179,'179Hf'),
(72,179):(72,178.945816,179,'179Hf'),
'180Hf':(72,179.946550,180,'180Hf'),
(72,180):(72,179.946550,180,'180Hf'),
'180Ta':(73,179.947465,180,'180Ta'),
(73,180):(73,179.947465,180,'180Ta'),
'181Ta':(73,180.947996,181,'181Ta'),
(73,181):(73,180.947996,181,'181Ta'),
'180W':(74,179.946704,180,'180W'),
(74,180):(74,179.946704,180,'180W'),
'182W':(74,181.948204,182,'182W'),
(74,182):(74,181.948204,182,'182W'),
'183W':(74,182.950223,183,'183W'),
(74,183):(74,182.950223,183,'183W'),
'184W':(74,183.950931,184,'184W'),
(74,184):(74,183.950931,184,'184W'),
'186W':(74,185.954364,186,'186W'),
(74,186):(74,185.954364,186,'186W'),
'185Re':(75,184.952955,185,'185Re'),
(75,185):(75,184.952955,185,'185Re'),
'187Re':(75,186.955753,187,'187Re'),
(75,187):(75,186.955753,187,'187Re'),
'184Os':(76,183.952489,184,'184Os'),
(76,184):(76,183.952489,184,'184Os'),
'186Os':(76,185.953838,186,'186Os'),
(76,186):(76,185.953838,186,'186Os'),
'187Os':(76,186.955750,187,'187Os'),
(76,187):(76,186.955750,187,'187Os'),
'188Os':(76,187.955838,188,'188Os'),
(76,188):(76,187.955838,188,'188Os'),
'189Os':(76,188.958147,189,'189Os'),
(76,189):(76,188.958147,189,'189Os'),
'190Os':(76,189.958447,190,'190Os'),
(76,190):(76,189.958447,190,'190Os'),
'192Os':(76,191.961481,192,'192Os'),
(76,192):(76,191.961481,192,'192Os'),
'191Ir':(77,190.960594,191,'191Ir'),
(77,191):(77,190.960594,191,'191Ir'),
'193Ir':(77,192.962926,193,'193Ir'),
(77,193):(77,192.962926,193,'193Ir'),
'190Pt':(78,189.959932,190,'190Pt'),
(78,190):(78,189.959932,190,'190Pt'),
'192Pt':(78,191.961038,192,'192Pt'),
(78,192):(78,191.961038,192,'192Pt'),
'194Pt':(78,193.962680,194,'194Pt'),
(78,194):(78,193.962680,194,'194Pt'),
'195Pt':(78,194.964791,195,'195Pt'),
(78,195):(78,194.964791,195,'195Pt'),
'196Pt':(78,195.964952,196,'196Pt'),
(78,196):(78,195.964952,196,'196Pt'),
'198Pt':(78,197.967893,198,'198Pt'),
(78,198):(78,197.967893,198,'198Pt'),
'197Au':(79,196.966569,197,'197Au'),
(79,197):(79,196.966569,197,'197Au'),
'196Hg':(80,195.965833,196,'196Hg'),
(80,196):(80,195.965833,196,'196Hg'),
'198Hg':(80,197.966769,198,'198Hg'),
(80,198):(80,197.966769,198,'198Hg'),
'199Hg':(80,198.968280,199,'199Hg'),
(80,199):(80,198.968280,199,'199Hg'),
'200Hg':(80,199.968326,200,'200Hg'),
(80,200):(80,199.968326,200,'200Hg'),
'201Hg':(80,200.970302,201,'201Hg'),
(80,201):(80,200.970302,201,'201Hg'),
'202Hg':(80,201.970643,202,'202Hg'),
(80,202):(80,201.970643,202,'202Hg'),
'204Hg':(80,203.973494,204,'204Hg'),
(80,204):(80,203.973494,204,'204Hg'),
'203Tl':(81,202.972344,203,'203Tl'),
(81,203):(81,202.972344,203,'203Tl'),
'205Tl':(81,204.974427,205,'205Tl'),
(81,205):(81,204.974427,205,'205Tl'),
'204Pb':(82,203.973044,204,'204Pb'),
(82,204):(82,203.973044,204,'204Pb'),
'206Pb':(82,205.974465,206,'206Pb'),
(82,206):(82,205.974465,206,'206Pb'),
'207Pb':(82,206.975897,207,'207Pb'),
(82,207):(82,206.975897,207,'207Pb'),
'208Pb':(82,207.976652,208,'208Pb'),
(82,208):(82,207.976652,208,'208Pb'),
'209Bi':(83,208.980399,209,'209Bi'),
(83,209):(83,208.980399,209,'209Bi'),
'232Th':(90,232.038055,232,'232Th'),
(90,232):(90,232.038055,232,'232Th'),
'231Pa':(91,231.035884,231,'231Pa'),
(91,231):(91,231.035884,231,'231Pa'),
'234U':(92,234.040952,234,'234U'),
(92,234):(92,234.040952,234,'234U'),
'235U':(92,235.043930,235,'235U'),
(92,235):(92,235.043930,235,'235U'),
'238U':(92,238.050788,238,'238U'),
(92,238):(92,238.050788,238,'238U'),
}
