pkgname = "sdbus-cpp"
pkgver = "2.3.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DSDBUSCPP_BUILD_CODEGEN=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = ["elogind-devel", "libexpat-devel"]
pkgdesc = "High-level C++ D-Bus library"
license = "LGPL-2.1-or-later"
url = "https://github.com/Kistler-Group/sdbus-cpp"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "3a289eded586c26d06c1387de72c7bf7c809527a70d51ba6401fe61059b19626"


@subpackage("sdbus-cpp-devel")
def _(self):
    return self.default_devel()
