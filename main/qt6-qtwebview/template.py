pkgname = "qt6-qtwebview"
pkgver = "6.9.2"
pkgrel = 0
build_style = "cmake"
# hangs for 2 minutes then fails on initing gl
make_check_args = ["-E", "(tst_qquickwebview)"]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = ["qt6-qtbase-private-devel", "qt6-qtwebengine-devel"]
pkgdesc = "Qt6 WebView component"
license = (
    "LGPL-2.1-only AND LGPL-3.0-only AND GPL-3.0-only WITH Qt-GPL-exception-1.0"
)
url = "https://www.qt.io"
source = f"https://download.qt.io/official_releases/qt/{pkgver[:-2]}/{pkgver}/submodules/qtwebview-everywhere-src-{pkgver}.tar.xz"
sha256 = "4ccfd14ae68222d5709e54c970da51d7f0b4cf58af045a96935dfcc34f1b1ff1"
# cross: TODO
options = ["!cross"]

if self.profile().arch in ["ppc64le"]:
    # mismatches
    options += ["!check"]


def init_check(self):
    self.make_check_env = {
        "QT_QPA_PLATFORM": "offscreen",
        "QML2_IMPORT_PATH": str(
            self.chroot_cwd / f"{self.make_dir}/lib/qt6/qml"
        ),
    }


@subpackage("qt6-qtwebview-devel")
def _(self):
    self.depends += [
        f"qt6-qtbase-devel~{pkgver[:-2]}",
        f"qt6-qtwebengine-devel~{pkgver[:-2]}",
    ]
    return self.default_devel(
        extra=[
            "usr/lib/qt6/metatypes",
            "usr/lib/qt6/mkspecs",
            "usr/lib/qt6/modules",
            "usr/lib/*.prl",
        ]
    )
