pkgname = "qt6-qt5compat"
pkgver = "6.6.3"
pkgrel = 0
build_style = "cmake"
# FIXME: times out after 5 minutes on aarch64
make_check_args = ["-E", "tst_qxmlinputsource"]
hostmakedepends = ["cmake", "ninja", "pkgconf", "qt6-qtbase"]
makedepends = ["qt6-qtdeclarative-devel"]
pkgdesc = "Module containing unsupported Qt5 APIs"
maintainer = "aurelia <git@elia.garden>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qt5compat-everywhere-src-{pkgver}.tar.xz"
sha256 = "68c2cf4e5eabfea27626fe40d088cb0dbb2c0414d3961ef132b7e06c60ceec0b"


def post_install(self):
    self.rm(self.destdir / "usr/tests", recursive=True)


@subpackage("qt6-qt5compat-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
