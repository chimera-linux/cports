pkgname = "qt6-qt5compat"
pkgver = "6.9.2"
pkgrel = 0
build_style = "cmake"
# FIXME: times out after 5 minutes on aarch64
make_check_args = ["-E", "(tst_qxmlinputsource|module_includes)"]
hostmakedepends = ["cmake", "ninja", "pkgconf", "qt6-qtbase"]
makedepends = ["qt6-qtbase-private-devel", "qt6-qtdeclarative-devel"]
pkgdesc = "Module containing unsupported Qt5 APIs"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qt5compat-everywhere-src-{pkgver}.tar.xz"
sha256 = "cb289905c689fc271ce783f8b67844040aa73d78f4f0cf8421fa713390a75b60"


def post_install(self):
    self.uninstall("usr/tests")


@subpackage("qt6-qt5compat-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
