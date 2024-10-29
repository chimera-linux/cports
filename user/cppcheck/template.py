pkgname = "cppcheck"
pkgver = "2.16.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DUSE_MATCHCOMPILER=ON",
    "-DFILESDIR=/usr/share/cppcheck",
    "-DBUILD_GUI=ON",
    "-DUSE_QT6=ON",
    "-DWITH_QCHART=ON",
    "-DBUILD_TESTS=ON",
    "-DUSE_BUNDLED_TINYXML2=OFF",
]
# racy in parallel
make_check_args = ["-j1"]
hostmakedepends = [
    "cmake",
    "docbook-xsl-nons",
    "ninja",
    "pkgconf",
    "xsltproc",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qtcharts-devel",
    "qt6-qttools-devel",
    "tinyxml2-devel",
]
pkgdesc = "Static analysis of C/C++ code"
maintainer = "xunil-cloud <river_electron@proton.me>"
license = "GPL-3.0-or-later"
url = "https://cppcheck.sourceforge.io"
source = f"https://github.com/danmar/cppcheck/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "f1a97c8cef5ee9d0abb57e9244549d4fe18d4ecac80cf82e250d1fc5f38b1501"
# TestSymbolDatabase::enum14 test failed
# (0x7FFFFFFFFFFFFFFF + 1 cause signed overflow)
hardening = ["!int"]


def post_build(self):
    self.do(
        "make", "DB2MAN=/usr/share/xsl-nons/docbook/manpages/docbook.xsl", "man"
    )


def post_install(self):
    self.install_man("cppcheck.1")


@subpackage("cppcheck-gui")
def _(self):
    self.subdesc = "GUI tool"
    self.depends = [self.parent]

    return [
        "usr/bin/cppcheck-gui",
        "usr/share/applications",
        "usr/share/cppcheck/translations",
        "usr/share/icons",
    ]
