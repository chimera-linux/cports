pkgname = "okular"
pkgver = "24.05.0"
pkgrel = 1
build_style = "cmake"
# FIXME segfaults/weird failures
make_check_args = [
    "-E",
    "(parttest|visibilitytest|signunsignedfieldtest|documenttest|mainshelltest|annotationtoolbartest|epubgeneratortest)",
]
make_check_wrapper = [
    "dbus-run-session",
    "--",
    "wlheadless-run",
    "--",
]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "discount-devel",
    "djvulibre-devel",
    "ebook-tools-devel",
    "karchive-devel",
    "kbookmarks-devel",
    "kcompletion-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdegraphics-mobipocket-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kparts-devel",
    "kpty-devel",
    "ktextwidgets-devel",
    "kwallet-devel",
    "kwindowsystem-devel",
    "kxmlgui-devel",
    "libkexiv2-devel",
    "libspectre-devel",
    "libzip-devel",
    "phonon-devel",
    "plasma-activities-devel",
    "poppler-qt-devel",
    "purpose-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtspeech-devel",
    "qt6-qtsvg-devel",
    "threadweaver-devel",
]
checkdepends = ["dbus", "xwayland-run"]
pkgdesc = "KDE document viewer"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/okular"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/okular-{pkgver}.tar.xz"
sha256 = "6f322f78de2aa0a4079351fe4651c080bd98d27eeb7f9dcc37765271b4a3ac80"
tool_flags = {"CFLAGS": ["-D_GNU_SOURCE"]}
# CFI: crashes tests
hardening = ["vis", "!cfi"]
# TODO
options = ["!cross"]


@subpackage("okular-devel")
def _devel(self):
    self.depends += [
        "kconfig-devel",
        "kcoreaddons-devel",
        "kxmlgui-devel",
        "qt6-qtbase-devel",
    ]
    return self.default_devel()
