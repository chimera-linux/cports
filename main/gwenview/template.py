pkgname = "gwenview"
pkgver = "25.08.1"
pkgrel = 1
build_style = "cmake"
make_check_args = [
    "-E",
    "(placetreemodeltest|urlutilstest|contextmanagertest)",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "baloo-devel",
    # "cfitsio-devel",
    "exiv2-devel",
    "kcrash-devel",
    "kdoctools-devel",
    "kguiaddons-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kimageannotator-devel",
    "kio-devel",
    "kitemmodels-devel",
    "knotifications-devel",
    "kparts-devel",
    "kwidgetsaddons-devel",
    "kwindowsystem-devel",
    "lcms2-devel",
    "libkdcraw-devel",
    "libtiff-devel",
    "phonon-devel",
    "plasma-activities-devel",
    "purpose-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtmultimedia-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwayland-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "KDE image viewer"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/gwenview"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/gwenview-{pkgver}.tar.xz"
sha256 = "4d92eef8fd543930cff6810062bc1d9ff103394247516bfef1edcd1bd67ad67c"
# avoid crash in raw thumbnailer
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
hardening = ["vis"]
# TODO
options = ["!cross"]
