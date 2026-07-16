pkgname = "ktexteditor"
pkgver = "6.28.0"
pkgrel = 0
build_style = "cmake"
make_check_args = [
    "-E",
    # FIXME: katedocument_test testAboutToSave() hangs for 5 minutes,
    "katedocument_test",
    # flaky tests when parallel
    "-j1",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = ["cmake", "extra-cmake-modules", "gettext", "ninja"]
makedepends = [
    "editorconfig-devel",
    "karchive-devel",
    "kauth-devel",
    "kconfig-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kio-devel",
    "kparts-devel",
    "ktextwidgets-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtspeech-devel",
    "qt6-qttools-devel",
    "sonnet-devel",
    "syntax-highlighting-devel",
]
checkdepends = ["dbus"]
pkgdesc = "KDE Full text editor component"
license = "LGPL-2.0-or-later AND (LGPL-2.0-only OR LGPL-3.0-only)"
url = "https://api.kde.org/frameworks/ktexteditor/html"
source = f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/ktexteditor-{pkgver}.tar.xz"
sha256 = "63b7bbd9325cfda64e2c8f862e2327270ef7a9d1f887b5c6585f372511d33f8d"
hardening = ["vis"]


@subpackage("ktexteditor-devel")
def _(self):
    self.depends += ["kparts-devel", "syntax-highlighting-devel"]

    return self.default_devel()
