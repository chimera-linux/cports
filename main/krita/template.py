pkgname = "krita"
pkgver = "6.0.2.1"
pkgrel = 1
build_style = "cmake"
configure_args = ["-DALLOW_UNSTABLE=QT6", "-DBUILD_WITH_QT6=ON"]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "python",
    "python-sip",
    "wayland-progs",
]
makedepends = [
    "boost-devel",
    "cups-devel",
    "eigen",
    "exiv2-devel",
    "fftw-devel",
    "fontconfig-devel",
    "freetype-devel",
    "fribidi-devel",
    "gsl-devel",
    "harfbuzz-devel",
    "immer",
    "kcolorscheme-devel",
    "kcompletion-devel",
    "kconfig-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kitemviews-devel",
    "kseexpr-devel",
    "kwidgetsaddons-devel",
    "lager",
    "lcms2-devel",
    "libheif-devel",
    "libjxl-devel",
    "libkdcraw-devel",
    "libmypaint-devel",
    "libpng-devel",
    "libtiff-devel",
    "libunibreak-devel",
    "libwebp-devel",
    "libxkbcommon-devel",
    "mesa-devel",
    "mlt-devel",
    "opencolorio-devel",
    "openexr-devel",
    "openjpeg-devel",
    "poppler-devel",
    "python-pyqt6",
    "qt6-qt5compat-devel",
    "qt6-qtbase-devel",
    "qt6-qtbase-private-devel",
    "qt6-qtsvg-devel",
    "quazip-devel",
    "sdl2-compat-devel",
    "wayland-devel",
    "wayland-protocols",
    "xsimd",
    "zlib-ng-compat-devel",
    "zug",
]
pkgdesc = "Digital painting program"
license = "GPL-2.0-or-later"
url = "https://krita.org"
source = f"$(KDE_SITE)/krita/{pkgver}/krita-{pkgver}.tar.xz"
sha256 = "f77daae0290c387063fafe1d2084517ddb0490d077dc0e6a2bd4f75e5dd5a100"
hardening = ["!int"]
# 1/3 of tests just crash
options = ["!check"]
