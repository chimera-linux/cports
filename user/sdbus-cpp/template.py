pkgname = "sdbus-cpp"
pkgver = "2.3.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DSDBUSCPP_BUILD_CODEGEN=ON", "-DSDBUSCPP_BUILD_TESTS=ON"]
# needs a bus
make_check_args = ["-E", ".*integration-tests"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["elogind-devel", "libexpat-devel"]
checkdepends = ["gtest-devel"]
pkgdesc = "D-Bus library for C++"
license = "LGPL-2.1-or-later"
url = "https://github.com/Kistler-Group/sdbus-cpp"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3a289eded586c26d06c1387de72c7bf7c809527a70d51ba6401fe61059b19626"


def post_install(self):
    # test remains
    self.uninstall("etc/dbus-1")
    self.uninstall("usr/tests")


@subpackage("sdbus-cpp-devel")
def _(self):
    return self.default_devel(extra=["cmd:sdbus-c++-xml2cpp"])
