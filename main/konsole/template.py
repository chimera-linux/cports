pkgname = "konsole"
pkgver = "25.08.3"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-E", "(TerminalInterfaceTest|PtyTest)"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "kbookmarks-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kglobalaccel-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kparts-devel",
    "kpty-devel",
    "ktextwidgets-devel",
    "qt6-qt5compat-devel",
    "qt6-qtmultimedia-devel",
]
pkgdesc = "KDE's Terminal Emulator"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/konsole"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/konsole-{pkgver}.tar.xz"
sha256 = "095a7ff10df3c70779b356fb3b5984062bbc698bbed966230e3dbccf6af36615"
hardening = ["vis"]
