pkgname = "sdbus-cpp"
pkgver = "2.1.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DSDBUSCPP_SDBUS_LIB=elogind",
    "-DSDBUSCPP_BUILD_CODEGEN=OFF",
    "-DSDBUSCPP_BUILD_DOCS=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "elogind-devel",
]
pkgdesc = "High-level C++ D-Bus library built on sd-bus"
license = "LGPL-2.1-or-later"
url = "https://github.com/Kistler-Group/sdbus-cpp"
source = f"https://github.com/Kistler-Group/sdbus-cpp/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "6025e5dc6cddd532ff960d14e68ced5f42a1916b23a73fea6bcb437f06992eaf"


@subpackage("sdbus-cpp-devel")
def _(self):
    return self.default_devel()
