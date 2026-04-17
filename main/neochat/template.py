pkgname = "neochat"
pkgver = "26.04.3"
pkgrel = 0
build_style = "cmake"
# depends on qthttpserver, which is not packaged
configure_args = ["-DBUILD_TESTING=OFF"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
]
makedepends = [
    "cmark-devel",
    "kcolorscheme-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "kirigami-addons-devel",
    "kirigami-devel",
    "kitemmodels-devel",
    "knotifications-devel",
    "kquickcharts-devel",
    "kquickimageeditor-devel",
    "kunifiedpush-devel",
    "kwindowsystem-devel",
    "libquotient-devel",
    "prison-devel",
    "purpose-devel",
    "qcoro-devel",
    "qqc2-desktop-style-devel",
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qtlocation-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtspeech-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwebview-devel",
    "syntax-highlighting-devel",
]
depends = [
    "qt6-qtlocation",
]
pkgdesc = "Matrix client"
license = "GPL-3.0-only"
url = "https://apps.kde.org/neochat"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/neochat-{pkgver}.tar.xz"
sha256 = "7813106878bde5286f45c005647048217b2e46444c8ac2ef76480a2de88e7f0f"
