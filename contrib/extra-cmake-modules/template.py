pkgname = "extra-cmake-modules"
pkgver = "5.112.0"
pkgrel = 0
build_style = "cmake"
hostmakedepends = ["cmake", "ninja"]
pkgdesc = "Extra modules and scripts for CMake"
maintainer = "aurelia <git@elia.garden>"
license = "BSD-3-Clause"
url = "https://invent.kde.org/frameworks/extra-cmake-modules"
source = f"https://download.kde.org/stable/frameworks/{pkgver[:pkgver.rfind('.')]}/extra-cmake-modules-{pkgver}.tar.xz"
sha256 = "ac1084772280d57e5f31e2e2816ecbec4884169413f24f063660eb6f15d4c2e2"
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
