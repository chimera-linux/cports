pkgname = "kdsoap"
pkgver = "2.3.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DKDSoap_QT6=ON",
    "-DKDSoap_EXAMPLES=OFF",
    "-DKDSoap_TESTS=ON",
]
# needs internet
# msexchange: hangs sometimes
make_check_args = [
    "-E",
    "(kdsoap-test_calc|kdsoap-test_webcalls|test_msexchange)",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "qt6-qtbase",
]
makedepends = [
    "qt6-qtbase-devel",
]
pkgdesc = "Qt-based SOAP component"
license = "MIT"
url = "https://www.kdab.com/development-resources/qt-tools/kd-soap"
source = f"https://github.com/KDAB/KDSoap/releases/download/kdsoap-{pkgver}/kdsoap-{pkgver}.tar.gz"
sha256 = "d2184951145cb768cc30376a10701be13869a164c1272d09f831ba2d195f02de"
# set in release
tool_flags = {"CFLAGS": ["-DNDEBUG"], "CXXFLAGS": ["-DNDEBUG"]}
# CFI: breaks build
hardening = ["vis", "!cfi"]


def post_install(self):
    self.install_license("LICENSE.txt")


@subpackage("kdsoap-devel")
def _(self):
    self.depends += ["qt6-qtbase-devel"]
    return self.default_devel()
