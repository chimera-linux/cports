pkgname = "ktexteditor"
pkgver = "6.18.0"
pkgrel = 0
build_style = "cmake"
# XXX drop libexec
configure_args = ["-DCMAKE_INSTALL_LIBEXECDIR=/usr/lib"]
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
sha256 = "4f8abb0436a0c6ca501f7be391975756cb07f8e403d3afe7ec2f02d12bf7b516"
hardening = ["vis"]


@subpackage("ktexteditor-devel")
def _(self):
    self.depends += ["kparts-devel", "syntax-highlighting-devel"]

    return self.default_devel()
