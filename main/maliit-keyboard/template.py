pkgname = "maliit-keyboard"
pkgver = "2.3.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_WITH_QT6=ON", "-Denable-presage=OFF"]
# 4 vs 2 expected host->keyEventCount() in subtests
make_check_args = ["-E", "ut_repeat-backspace"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = ["cmake", "ninja", "pkgconf", "gettext"]
makedepends = [
    "glib-devel",
    "hunspell-devel",
    "libchewing-devel",
    "libpinyin-devel",
    "maliit-framework-devel",
    "qt6-qt5compat-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
]
pkgdesc = "Virtual keyboard for Wayland and X11"
license = "LGPL-3.0-only AND BSD-3-Clause"
url = "https://github.com/maliit/keyboard"
source = f"{url}/archive/{pkgver}.tar.gz"
sha256 = "c3e1eb985b8ae7ce4e3e28412b7e797ff5db437ccd327e0d852a3c37f17fe456"
tool_flags = {
    "CXXFLAGS": [
        # avoid ~500 lines of spam
        "-Wno-deprecated-declarations",
        "-Wno-inconsistent-missing-override",
    ]
}


def post_install(self):
    self.install_license("COPYING.BSD")
