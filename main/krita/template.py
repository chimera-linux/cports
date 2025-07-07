pkgname = "krita"
pkgver = "0_git20250707"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_WITH_QT6=ON",
    "-DBUILD_TESTING=OFF",
]
makedepends = [
    "cmake",
    "extra-cmake-modules",
    "ninja",
    "pkgconf",
    "kconfig-devel",
    "kcompletion-devel",
    "kcoreaddons-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kitemviews-devel",
    "kcrash-devel",
    "kitemmodels-devel",
    "kwidgetsaddons-devel",
    "kcolorscheme-devel",
    "gettext-devel",
    "kwindowsystem-devel",
    "python-devel",
    "boost-devel",
    "immer",
    "lager",
    "zug",
    "python-sip",
    "qt6-qtbase-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtsvg-devel",
    "qt6-qt5compat-devel",
    "qt6-qtwayland-devel",
    "gsl-devel",
    "libwebp-devel",
    "openexr-devel",
    "openjpeg-devel",
    "fftw-devel",
    "libheif-devel",
    "libjxl-devel",
    "opencolorio-devel",
    "exiv2-devel",
    "python-pyqt6",
    "libmypaint-devel",
    "libunibreak-devel",
    "libkdcraw-devel",
    "quazip-devel",
    "xsimd",
    "poppler-devel",
    "eigen",
]
pkgdesc = "Digital painting program"
license = "GPL-2.0-or-later"
url = "https://krita.org"
_commit = "9d4fcc7a2013e8b0d060f9389ca0b92ab72fdc47"
source = f"https://invent.kde.org/graphics/krita/-/archive/{_commit}/krita-{_commit}.tar.gz"
sha256 = "f87d91d2edf9adb4d6c9dbdd73dd3ff702707103d8ca4f878322914445f4a84b"
# !check: just want to get it building first
# !distlicense: maybe unnecessary, didn't want to risk having to rebuild since
#   it takes ages
options = ["!check", "!distlicense"]
