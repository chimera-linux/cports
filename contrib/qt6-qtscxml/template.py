pkgname = "qt6-qtscxml"
pkgver = "6.7.2"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DQT_BUILD_TESTS=ON"]
make_check_args = [
    "-E",
    "(module_includes|test_qtscxml_module|tst_scion|tst_qstatemachine)",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
    "perl",
    "qt6-qtbase",
    "qt6-qtdeclarative-devel",
]
makedepends = [
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
]
pkgdesc = "Qt6 SCXML component"
maintainer = "psykose <alice@ayaya.dev>"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtscxml-everywhere-src-{pkgver}.tar.xz"
sha256 = "20ecf93506d48f27b492ad3dd9d88830e08d642faec3071ce53396a8ae05c86f"


def init_check(self):
    self.make_check_env = {
        "QML2_IMPORT_PATH": str(
            self.chroot_cwd / f"{self.make_dir}/lib/qt6/qml"
        ),
        "QT_QPA_PLATFORM": "offscreen",
    }


def post_install(self):
    self.uninstall("usr/tests")


@subpackage("qt6-qtscxml-devel")
def _devel(self):
    return self.default_devel(
        extra=[
            "usr/lib/qt6/libexec",
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
