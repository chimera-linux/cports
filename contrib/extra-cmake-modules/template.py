pkgname = "extra-cmake-modules"
pkgver = "6.2.0"
pkgrel = 0
build_style = "cmake"
# who knows why these fail
make_check_args = [
    "-E",
    "(ExecuteKDEModules"
    "|KDEFetchTranslations"
    "|KDEInstallDirsTest.not_cache_variable"
    "|KDEInstallDirsTest.vars_in_sync_cmake_arg"
    "|KDEInstallDirsTest.vars_in_sync_kde_arg"
    "|KDEInstallDirsTest.vars_in_sync_no_args"
    "|ecm_add_tests-multi_tests"
    "|ecm_add_tests-single_tests"
    "|ecm_add_tests_did_run-multi_tests"
    "|ecm_add_tests_did_run-single_tests)",
]
hostmakedepends = ["cmake", "ninja"]
checkdepends = ["qt6-qtbase"]
pkgdesc = "Extra modules and scripts for CMake"
maintainer = "aurelia <git@elia.garden>"
license = "BSD-3-Clause"
url = "https://invent.kde.org/frameworks/extra-cmake-modules"
source = f"$(KDE_SITE)/frameworks/{pkgver[:pkgver.rfind('.')]}/extra-cmake-modules-{pkgver}.tar.xz"
sha256 = "6374bfa0dded8be265c702acd5de11eecd2851c625b93e1c87d8d0f5f1a8ebe1"


def post_install(self):
    self.install_license("COPYING-CMAKE-SCRIPTS")
