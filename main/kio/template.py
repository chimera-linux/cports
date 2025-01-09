pkgname = "kio"
pkgver = "6.9.0"
pkgrel = 0
build_style = "cmake"
# flaky
make_check_args = ["-E", "kiocore-krecentdocumenttest"]
make_check_wrapper = ["dbus-run-session"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "acl-devel",
    "karchive-devel",
    "kauth-devel",
    "kbookmarks-devel",
    "kcolorscheme-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kded-devel",
    "kdoctools-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kitemviews-devel",
    "kjobwidgets-devel",
    "kservice-devel",
    "kwallet-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "libxslt-devel",
    "qt6-qt5compat-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
    "solid-devel",
]
depends = ["kded"]
checkdepends = ["dbus"]
pkgdesc = "KDE Network transparent access to files and data"
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = (
    "LGPL-2.1-only AND LGPL-2.1-or-later AND (LGPL-2.1-only OR LGPL-3.0-only)"
)
url = "https://api.kde.org/frameworks/kio/html"
source = (
    f"$(KDE_SITE)/frameworks/{pkgver[: pkgver.rfind('.')]}/kio-{pkgver}.tar.xz"
)
sha256 = "5360962b0b9bc06d01f86888c896ca591ccd2d0bca79b7f5cc4367a6e31b368b"
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
hardening = ["vis"]
# >60% (40/62) tests fail, pain to get working in a limited enviroment due to expecting e.g. real disks
options = ["!check"]


@subpackage("kio-devel")
def _(self):
    self.depends += [
        "kbookmarks-devel",
        "kcompletion-devel",
        "kconfig-devel",
        "kcoreaddons-devel",
        "kitemviews-devel",
        "kjobwidgets-devel",
        "kservice-devel",
        "kwindowsystem-devel",
        "solid-devel",
    ]

    return self.default_devel()
