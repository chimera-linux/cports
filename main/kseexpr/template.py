pkgname = "kseexpr"
pkgver = "6.0.0.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_DEMOS=OFF",
    "-DBUILD_TESTS=ON",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "python",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qttools-devel",
]
checkdepends = ["gtest-devel"]
pkgdesc = "Krita fork of an embeddable expression evaluation engine"
license = "GPL-3.0-or-later"
url = "https://krita.org"
# source = f"$(KDE_SITE)/kseexpr/{pkgver}/src/kseexpr-{pkgver}.tar.gz"
source = f"https://invent.kde.org/graphics/kseexpr/-/archive/v{pkgver}/kseexpr-v{pkgver}.tar.gz"
sha256 = "60f84d26f922b65951a81cfb37323040927c5f01101a60f9563573016e0a52b8"
# FIXME tests fail in buildInterpreter(), vector.emplace_back()
tool_flags = {
    "CXXFLAGS": ["-D_LIBCPP_HARDENING_MODE=_LIBCPP_HARDENING_MODE_NONE"]
}


def post_install(self):
    self.uninstall("usr/share/test")


@subpackage("kseexpr-devel")
def _(self):
    return self.default_devel()
