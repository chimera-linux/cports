[1m[93mmain/python-numpy/patches/no-include-highway.patch[39m[0m[2m --- 1/2 --- Text[0m
[2m2 [0m                                                                                [2m 2 [0m
[2m3 [0malso a workaround for loongarch, highway.h fails to include                     [2m 3 [0malso a workaround for loongarch, highway.h fails to include
[2m4 [0m                                                                                [2m 4 [0m
[2m. [0m                                                                                [92;1m 5 [0m[92;1mdiff[0m[92;1m [0m[92;1m-ruN[0m[92;1m [0m[92;1ma[0m[92;1m/[0m[92;1mnumpy[0m[92;1m/[0m[92;1m_core[0m[92;1m/[0m[92;1msrc[0m[92;1m/[0m[92;1mnpysort[0m[92;1m/[0m[92;1mhighway_qsort[0m[92;1m.[0m[92;1mhpp[0m[92;1m.[0m[92;1mrej[0m[92;1m [0m[92;1mb[0m[92;1m/[0m[92;1mnumpy[0m[92;1m/[0m[92;1m_core[0m[92;1m/[0m[92;1msrc[0m[92;1m/[0m[92;1mnpy[0m
[2m. [0m                                                                                [92;1m[2m . [0m[0m[92;1msort[0m[92;1m/[0m[92;1mhighway_qsort[0m[92;1m.[0m[92;1mhpp[0m[92;1m.[0m[92;1mrej[0m
[91;1m5 [0m[91m---[0m[91m [0m[91ma[0m[91m/[0m[91mnumpy[0m[91m/[0m[91m_core[0m[91m/[0m[91msrc[0m[91m/[0m[91mumath[0m[91m/[0m[91mloops_trigonometric[0m[91m.[0m[91mdispatch[0m[91m.[0m[91mcpp[0m                    [92;1m 6 [0m[92m---[0m[92m [0m[92ma[0m[92m/[0m[92mnumpy[0m[92m/[0m[92m_core[0m[92m/[0m[92msrc[0m[92m/[0m[92;1mnpysort[0m[92;1m/[0m[92;1mhighway_qsort[0m[92;1m.[0m[92;1mhpp[0m[92;1m.[0m[92;1mrej[0m[92;1m    [0m[92;1m1970-01-01[0m[92;1m [0m[92;1m01[0m[92;1m:[0m[92;1m00[0m[92;1m:[0m[92;1m00[0m[92;1m.[0m[92;1m0000[0m
[91;1m[2m. [0m[0m                                                                                [92;1m[2m . [0m[0m[92;1m00000[0m[92;1m [0m[92;1m+[0m[92;1m0100[0m
[2m. [0m                                                                                [92;1m 7 [0m[92;1m+[0m[92;1m+[0m[92;1m+[0m[92;1m [0m[92;1mb[0m[92;1m/[0m[92;1mnumpy[0m[92;1m/[0m[92;1m_core[0m[92;1m/[0m[92;1msrc[0m[92;1m/[0m[92;1mnpysort[0m[92;1m/[0m[92;1mhighway_qsort[0m[92;1m.[0m[92;1mhpp[0m[92;1m.[0m[92;1mrej[0m[92;1m    [0m[92;1m2025-05-15[0m[92;1m [0m[92;1m12[0m[92;1m:[0m[92;1m07[0m[92;1m:[0m[92;1m28[0m[92;1m.[0m[92;1m3980[0m
[2m. [0m                                                                                [92;1m[2m . [0m[0m[92;1m20432[0m[92;1m [0m[92;1m+[0m[92;1m0200[0m
[2m. [0m                                                                                [92;1m 8 [0m[92;1m@[0m[92;1m@[0m[92;1m [0m[92;1m-0[0m[92;1m,[0m[92;1m0[0m[92;1m [0m[92;1m+[0m[92;1m1[0m[92;1m,[0m[92;1m21[0m[92;1m [0m[92;1m@[0m[92;1m@[0m
[2m. [0m                                                                                [92;1m 9 [0m[92;1m+[0m[92;1m@[0m[92;1m@[0m[92;1m [0m[92;1m-2[0m[92;1m,[0m[92;1m14[0m[92;1m [0m[92;1m+[0m[92;1m2[0m[92;1m,[0m[92;1m20[0m[92;1m [0m[92;1m@[0m[92;1m@[0m
[2m. [0m                                                                                [92;1m10 [0m[92;1m+[0m[92;1m [0m[92;1m#[0m[92;1mdefine[0m[92;1m [0m[92;1mNUMPY_SRC_COMMON_NPYSORT_HWY_SIMD_QSORT_HPP[0m
[2m. [0m                                                                                [92;1m11 [0m[92;1m+[0m[92;1m [0m
[2m. [0m                                                                                [92;1m12 [0m[92;1m+[0m[92;1m [0m[92;1m#[0m[92;1mdefine[0m[92;1m [0m[92;1mVQSORT_ONLY_STATIC[0m[92;1m [0m[92;1m1[0m
[2m. [0m                                                                                [92;1m13 [0m[92;1m+[0m[92;1m+[0m[92;1m#[0m[92;1mifdef[0m[92;1m [0m[92;1m__loongarch__[0m
[2m. [0m                                                                                [92;1m14 [0m[92;1m+[0m[92;1m+[0m[92;1m#[0m[92;1mdefine[0m[92;1m [0m[92;1mNPY_DISABLE_HIGHWAY_SORT[0m
[2m. [0m                                                                                [92;1m15 [0m[92;1m+[0m[92;1m+[0m[92;1m#[0m[92;1melse[0m
[2m. [0m                                                                                [92;1m16 [0m[92;1m+[0m[92;1m [0m[92;1m#[0m[92;1minclude[0m[92;1m [0m[92;1m"[0m[92;1mhwy[0m[92;1m/[0m[92;1mhighway[0m[92;1m.[0m[92;1mh[0m[92;1m"[0m
[2m. [0m                                                                                [92;1m17 [0m[92;1m+[0m[92;1m [0m[92;1m#[0m[92;1minclude[0m[92;1m [0m[92;1m"[0m[92;1mhwy[0m[92;1m/[0m[92;1mcontrib[0m[92;1m/[0m[92;1msort[0m[92;1m/[0m[92;1mvqsort-inl[0m[92;1m.[0m[92;1mh[0m[92;1m"[0m
[2m. [0m                                                                                [92;1m18 [0m[92;1m+[0m[92;1m+[0m[92;1m#[0m[92;1mendif[0m
[2m. [0m                                                                                [92;1m19 [0m[92;1m+[0m[92;1m [0m
[2m. [0m                                                                                [92;1m20 [0m[92;1m+[0m[92;1m [0m[92;1m#[0m[92;1minclude[0m[92;1m [0m[92;1m"[0m[92;1mcommon[0m[92;1m.[0m[92;1mhpp[0m[92;1m"[0m
[2m. [0m                                                                                [92;1m21 [0m[92;1m+[0m[92;1m [0m
[2m. [0m                                                                                [92;1m22 [0m[92;1m+[0m[92;1m+[0m[92;1m#[0m[92;1mifndef[0m[92;1m [0m[92;1mNPY_DISABLE_HIGHWAY_SORT[0m
[2m. [0m                                                                                [92;1m23 [0m[92;1m+[0m[92;1m [0m[92;1m#[0m[92;1mif[0m[92;1m [0m[92;1m![0m[92;1mVQSORT_COMPILER_COMPATIBLE[0m
[2m. [0m                                                                                [92;1m24 [0m[92;1m+[0m[92;1m [0m[92;1m#[0m[92;1mdefine[0m[92;1m [0m[92;1mNPY_DISABLE_HIGHWAY_SORT[0m
[2m. [0m                                                                                [92;1m25 [0m[92;1m+[0m[92;1m [0m[92;1m#[0m[92;1mendif[0m
[2m. [0m                                                                                [92;1m26 [0m[92;1m+[0m[92;1m+[0m[92;1m#[0m[92;1mendif[0m
[2m. [0m                                                                                [92;1m27 [0m[92;1m+[0m[92;1m [0m
[2m. [0m                                                                                [92;1m28 [0m[92;1m+[0m[92;1m [0m[92;1m#[0m[92;1mifndef[0m[92;1m [0m[92;1mNPY_DISABLE_HIGHWAY_SORT[0m
[2m. [0m                                                                                [92;1m29 [0m[92;1m+[0m[92;1m [0m[92;1mnamespace[0m[92;1m [0m[92;1mnp[0m[92;1m [0m[92;1m{[0m[92;1m [0m[92;1mnamespace[0m[92;1m [0m[92;1mhighway[0m[92;1m [0m[92;1m{[0m[92;1m [0m[92;1mnamespace[0m[92;1m [0m[92;1mqsort_simd[0m[92;1m [0m[92;1m{[0m
[2m. [0m                                                                                [92;1m30 [0m[92;1mdiff[0m[92;1m [0m[92;1m-ruN[0m[92;1m [0m[92;1ma[0m[92;1m/[0m[92;1mnumpy[0m[92;1m/[0m[92;1m_core[0m[92;1m/[0m[92;1msrc[0m[92;1m/[0m[92mumath[0m[92m/[0m[92mloops_trigonometric[0m[92m.[0m[92mdispatch[0m[92m.[0m[92mcpp[0m[92;1m [0m[92;1mb[0m[92;1m/[0m[92;1mnumpy[0m[92;1m/[0m[92;1m_cor[0m
[2m. [0m                                                                                [92;1m[2m.. [0m[0m[92;1me[0m[92;1m/[0m[92;1msrc[0m[92;1m/[0m[92;1mumath[0m[92;1m/[0m[92;1mloops_trigonometric[0m[92;1m.[0m[92;1mdispatch[0m[92;1m.[0m[92;1mcpp[0m
[91;1m6 [0m[91m+[0m[91m+[0m[91m+[0m[91m [0m[91mb[0m[91m/[0m[91mnumpy[0m[91m/[0m[91m_core[0m[91m/[0m[91msrc[0m[91m/[0m[91mumath[0m[91m/[0m[91mloops_trigonometric[0m[91m.[0m[91mdispatch[0m[91m.[0m[91mcpp[0m                    [92;1m31 [0m[92;1m---[0m[92;1m [0m[92;1ma[0m[92;1m/[0m[92;1mnumpy[0m[92;1m/[0m[92;1m_core[0m[92;1m/[0m[92;1msrc[0m[92;1m/[0m[92;1mumath[0m[92;1m/[0m[92;1mloops_trigonometric[0m[92;1m.[0m[92;1mdispatch[0m[92;1m.[0m[92;1mcpp[0m[92;1m    [0m[92;1m2025-04-19[0m[92;1m [0m[92;1m21[0m[92;1m:[0m[92;1m3[0m
[91;1m[2m. [0m[0m                                                                                [92;1m[2m.. [0m[0m[92;1m0[0m[92;1m:[0m[92;1m11[0m[92;1m.[0m[92;1m000000000[0m[92;1m [0m[92m+[0m[92;1m0200[0m
[2m. [0m                                                                                [92;1m32 [0m[92m+[0m[92m+[0m[92;1m+[0m[92m [0m[92mb[0m[92m/[0m[92mnumpy[0m[92m/[0m[92m_core[0m[92m/[0m[92msrc[0m[92m/[0m[92mumath[0m[92m/[0m[92mloops_trigonometric[0m[92m.[0m[92mdispatch[0m[92m.[0m[92mcpp[0m[92;1m    [0m[92;1m2025-05-15[0m[92;1m [0m[92;1m12[0m[92;1m:[0m[92;1m0[0m
[2m. [0m                                                                                [92;1m[2m.. [0m[0m[92;1m7[0m[92;1m:[0m[92;1m28[0m[92;1m.[0m[92;1m398020432[0m[92;1m [0m[92;1m+[0m[92;1m0200[0m
[2m7 [0m@@ -3,8 +3,10 @@                                                                [2m33 [0m@@ -3,8 +3,10 @@
[2m8 [0m #include "loops_utils.h"                                                       [2m34 [0m #include "loops_utils.h"
[2m9 [0m                                                                                [2m35 [0m 

[1mmain/python-numpy/patches/no-include-highway.patch[0m[2m --- 2/2 --- Text[0m
[2m15 [0m[2m41 [0m 
[2m16 [0m[2m42 [0m /*
[2m17 [0m[2m43 [0m  * Vectorized approximate sine/cosine algorithms: The following code is a
[91;1m18 [0m[2m   [0m[91;1m---[0m[91;1m [0m[91;1ma[0m[91;1m/[0m[91;1mnumpy[0m[91;1m/[0m[91;1m_core[0m[91;1m/[0m[91;1msrc[0m[91;1m/[0m[91;1mnpysort[0m[91;1m/[0m[91;1mhighway_qsort[0m[91;1m.[0m[91;1mhpp[0m
[91;1m19 [0m[2m   [0m[91;1m+[0m[91;1m+[0m[91;1m+[0m[91;1m [0m[91;1mb[0m[91;1m/[0m[91;1mnumpy[0m[91;1m/[0m[91;1m_core[0m[91;1m/[0m[91;1msrc[0m[91;1m/[0m[91;1mnpysort[0m[91;1m/[0m[91;1mhighway_qsort[0m[91;1m.[0m[91;1mhpp[0m
[91;1m20 [0m[2m   [0m[91;1m@[0m[91;1m@[0m[91;1m [0m[91;1m-2[0m[91;1m,[0m[91;1m14[0m[91;1m [0m[91;1m+[0m[91;1m2[0m[91;1m,[0m[91;1m20[0m[91;1m [0m[91;1m@[0m[91;1m@[0m
[91;1m21 [0m[2m   [0m[91;1m [0m[91;1m#[0m[91;1mdefine[0m[91;1m [0m[91;1mNUMPY_SRC_COMMON_NPYSORT_HWY_SIMD_QSORT_HPP[0m
[91;1m22 [0m[2m   [0m[91;1m [0m
[91;1m23 [0m[2m   [0m[91;1m [0m[91;1m#[0m[91;1mdefine[0m[91;1m [0m[91;1mVQSORT_ONLY_STATIC[0m[91;1m [0m[91;1m1[0m
[91;1m24 [0m[2m   [0m[91;1m+[0m[91;1m#[0m[91;1mifdef[0m[91;1m [0m[91;1m__loongarch__[0m
[91;1m25 [0m[2m   [0m[91;1m+[0m[91;1m#[0m[91;1mdefine[0m[91;1m [0m[91;1mNPY_DISABLE_HIGHWAY_SORT[0m
[91;1m26 [0m[2m   [0m[91;1m+[0m[91;1m#[0m[91;1melse[0m
[91;1m27 [0m[2m   [0m[91;1m [0m[91;1m#[0m[91;1minclude[0m[91;1m [0m[91;1m"[0m[91;1mhwy[0m[91;1m/[0m[91;1mhighway[0m[91;1m.[0m[91;1mh[0m[91;1m"[0m
[91;1m28 [0m[2m   [0m[91;1m [0m[91;1m#[0m[91;1minclude[0m[91;1m [0m[91;1m"[0m[91;1mhwy[0m[91;1m/[0m[91;1mcontrib[0m[91;1m/[0m[91;1msort[0m[91;1m/[0m[91;1mvqsort-inl[0m[91;1m.[0m[91;1mh[0m[91;1m"[0m
[91;1m29 [0m[2m   [0m[91;1m+[0m[91;1m#[0m[91;1mendif[0m
[91;1m30 [0m[2m   [0m[91;1m [0m
[91;1m31 [0m[2m   [0m[91;1m [0m[91;1m#[0m[91;1minclude[0m[91;1m [0m[91;1m"[0m[91;1mcommon[0m[91;1m.[0m[91;1mhpp[0m[91;1m"[0m
[91;1m32 [0m[2m   [0m[91;1m [0m
[91;1m33 [0m[2m   [0m[91;1m+[0m[91;1m#[0m[91;1mifndef[0m[91;1m [0m[91;1mNPY_DISABLE_HIGHWAY_SORT[0m
[91;1m34 [0m[2m   [0m[91;1m [0m[91;1m#[0m[91;1mif[0m[91;1m [0m[91;1m![0m[91;1mVQSORT_COMPILER_COMPATIBLE[0m
[91;1m35 [0m[2m   [0m[91;1m [0m[91;1m#[0m[91;1mdefine[0m[91;1m [0m[91;1mNPY_DISABLE_HIGHWAY_SORT[0m
[91;1m36 [0m[2m   [0m[91;1m [0m[91;1m#[0m[91;1mendif[0m
[91;1m37 [0m[2m   [0m[91;1m+[0m[91;1m#[0m[91;1mendif[0m
[91;1m38 [0m[2m   [0m[91;1m [0m
[91;1m39 [0m[2m   [0m[91;1m [0m[91;1m#[0m[91;1mifndef[0m[91;1m [0m[91;1mNPY_DISABLE_HIGHWAY_SORT[0m
[91;1m40 [0m[2m   [0m[91;1m [0m[91;1mnamespace[0m[91;1m [0m[91;1mnp[0m[91;1m [0m[91;1m{[0m[91;1m [0m[91;1mnamespace[0m[91;1m [0m[91;1mhighway[0m[91;1m [0m[91;1m{[0m[91;1m [0m[91;1mnamespace[0m[91;1m [0m[91;1mqsort_simd[0m[91;1m [0m[91;1m{[0m

[1m[93mmain/python-numpy/template.py[39m[0m[2m --- 1/2 --- Python[0m
[2m1 [0mpkgname [1m=[0m [95m"python-numpy"[0m                                                         [2m1 [0mpkgname [1m=[0m [95m"python-numpy"[0m
[91;1m2 [0mpkgver [1m=[0m [91m"[0m[91m2[0m[91m.[0m[91m2[0m[91m.[0m[91;1;4m4[0m[91m"[0m                                                                 [92;1m2 [0mpkgver [1m=[0m [92m"[0m[92m2[0m[92m.[0m[92m2[0m[92m.[0m[92;1;4m5[0m[92m"[0m
[91;1m3 [0mpkgrel [1m=[0m [91m1[0m                                                                       [92;1m3 [0mpkgrel [1m=[0m [92m0[0m
[2m4 [0mbuild_style [1m=[0m [95m"python_pep517"[0m                                                    [2m4 [0mbuild_style [1m=[0m [95m"python_pep517"[0m
[2m5 [0mmake_build_args [1m=[0m []                                                             [2m5 [0mmake_build_args [1m=[0m []
[2m6 [0mhostmakedepends [1m=[0m [                                                              [2m6 [0mhostmakedepends [1m=[0m [

[1mmain/python-numpy/template.py[0m[2m --- 2/2 --- Python[0m
[2m20 [0mlicense [1m=[0m [95m"BSD-3-Clause"[0m                                                        [2m20 [0mlicense [1m=[0m [95m"BSD-3-Clause"[0m
[2m21 [0murl [1m=[0m [95m"https://numpy.org"[0m                                                       [2m21 [0murl [1m=[0m [95m"https://numpy.org"[0m
[2m22 [0msource [1m=[0m [95mf"https://github.com/numpy/numpy/releases/download/v{pkgver}/numpy-{pk[0m [2m22 [0msource [1m=[0m [95mf"https://github.com/numpy/numpy/releases/download/v{pkgver}/numpy-{pk[0m
[2m[2m.. [0m[0m[95mgver}.tar.gz"[0m                                                                   [2m[2m.. [0m[0m[95mgver}.tar.gz"[0m
[91;1m23 [0msha256 [1m=[0m [91m"9ba03692a45d3eef66559efe1d1096c4b9b75c0986b5dff5530c378fb8331d4f"[0m     [92;1m23 [0msha256 [1m=[0m [92m"a9c0d994680cd991b1cb772e8b297340085466a6fe964bc9d4e80f5e2f43c291"[0m
[2m24 [0mhardening [1m=[0m [[95m"!int"[0m]                                                            [2m24 [0mhardening [1m=[0m [[95m"!int"[0m]
[2m25 [0m                                                                                [2m25 [0m
[2m26 [0m[1mif[0m self.profile().arch [1min[0m [[95m"aarch64"[0m, [95m"loongarch64"[0m]:                           [2m26 [0m[1mif[0m self.profile().arch [1min[0m [[95m"aarch64"[0m, [95m"loongarch64"[0m]:

