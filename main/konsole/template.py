pkgname = "konsole"
pkgver = "24.08.2"
pkgrel = 0
build_style = "cmake"
make_check_args = ["-E", "TerminalInterfaceTest"]
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
maintainer = "Jami Kettunen <jami.kettunen@protonmail.com>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/konsole"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/konsole-{pkgver}.tar.xz"
sha256 = "ae72ca4e2d9123b9bada99d2d3b01398ff5082b549b38579cf9aa94c2bffd719"
hardening = ["vis"]
