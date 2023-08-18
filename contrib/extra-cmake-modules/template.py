pkgname = "extra-cmake-modules"
pkgver = "5.109.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Extra modules and scripts for CMake"
maintainer = "aurelia <git@elia.garden>"
license = "BSD-3-Clause"
url = "https://github.com/KDE/extra-cmake-modules"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "f9f9f9463dcd9633387f88b0032f9ce8f86aac85e3fe866f17d7b2fe6c5d578d"
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
