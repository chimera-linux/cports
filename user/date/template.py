pkgname = "date"
pkgver = "3.0.4"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_SHARED_LIBS=ON",
    "-DBUILD_TZ_LIB=ON",
    "-DUSE_SYSTEM_TZ_DB=ON",
    "-DENABLE_DATE_TESTING=ON",
]
make_check_target = "testit"
hostmakedepends = [
    "bash",
    "cmake",
    "ninja",
    "pkgconf",
]
pkgdesc = "Date and time library based on the C++11/14/17 <chrono> header"
license = "MIT"
url = "https://github.com/HowardHinnant/date"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "56e05531ee8994124eeb498d0e6a5e1c3b9d4fccbecdf555fe266631368fb55f"


@subpackage("date-devel")
def _(self):
    return self.default_devel()


def post_install(self):
    self.install_license("LICENSE.txt")
