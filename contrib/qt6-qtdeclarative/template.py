pkgname = "qt6-qtdeclarative"
pkgver = "6.5.0"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DQT_BUILD_TESTS=ON",
]
hostmakedepends = [
    "cmake", "ninja", "pkgconf", "perl", "python", "qt6-qtbase",
    "qt6-qtshadertools"
]
makedepends = ["qt6-qtbase-devel", "qt6-qtshadertools-devel"]
pkgdesc = "Qt6 declarative component"
license = "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtdeclarative-everywhere-src-{pkgver}.tar.xz"
sha256 = "f7d631cd8ebc1491dad0f30f1b5326ae812bee4ad706e61157816a82bf588c97"
debug_level = 1 # defatten, especially with LTO
# FIXME
hardening = ["!int"]
# TODO
options = ["!check", "!cross"]

def post_install(self):
    self.rm(self.destdir / "usr/tests", recursive = True)
    self.rm(self.destdir / "usr/lib/qt6/bin/testapp")
    for f in (self.destdir / "usr/lib/qt6/bin").glob("qqmldebug*"):
        f.unlink()

@subpackage("qt6-qtdeclarative-devel")
def _devel(self):
    self.depends += [
        f"qt6-qtshadertools-devel~{pkgver[:-2]}",
        f"qt6-qtbase-devel~{pkgver[:-2]}",
    ]

    return self.default_devel(extra = [
        "usr/lib/qt6/metatypes",
        "usr/lib/qt6/mkspecs",
        "usr/lib/qt6/modules",
        "usr/lib/qt6/plugins/qmltooling",
        "usr/lib/qt6/plugins/qmllint",
        "usr/lib/qt6/libexec/qmlcachegen",
        "usr/lib/qt6/libexec/qmlimportscanner",
        "usr/lib/qt6/libexec/qmltyperegistrar",
        "usr/lib/qt6/bin/qmlformat",
        "usr/lib/qt6/bin/qmllint",
        "usr/lib/qt6/bin/qmlpreview",
        "usr/lib/qt6/bin/qmlprofiler",
        "usr/lib/*.prl",
    ])
