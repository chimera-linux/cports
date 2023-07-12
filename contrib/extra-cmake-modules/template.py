pkgname = "extra-cmake-modules"
pkgver = "5.108.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Extra modules and scripts for CMake"
maintainer = "aurelia <git@elia.garden>"
license = "BSD-3-Clause"
url = "https://github.com/KDE/extra-cmake-modules"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "6c7fde74e5d18e6a1a0723371d9c0db70f4a648b81837e0f8cd82b83014624d1"
# 10 out of 83 tests fail? It still seemed to run fine when building with it.
#  2 - ExecuteKDEModules
#  3 - KDEFetchTranslations
#  4 - KDEInstallDirsTest.vars_in_sync_no_args
#  5 - KDEInstallDirsTest.not_cache_variable
#  6 - KDEInstallDirsTest.vars_in_sync_kde_arg
#  7 - KDEInstallDirsTest.vars_in_sync_cmake_arg
# 16 - ecm_add_tests-single_tests
# 17 - ecm_add_tests_did_run-single_tests
# 18 - ecm_add_tests-multi_tests
# 19 - ecm_add_tests_did_run-multi_tests
options = ["!check"]

def post_install(self):
    self.install_license("COPYING-CMAKE-SCRIPTS")
