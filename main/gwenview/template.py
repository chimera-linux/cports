pkgname = "gwenview"
pkgver = "24.12.2"
pkgrel = 0
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
    "qt6-qtsvg-devel",
    "qt6-qtwayland-devel",
    "wayland-devel",
    "wayland-protocols",
]
pkgdesc = "KDE image viewer"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/gwenview"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/gwenview-{pkgver}.tar.xz"
sha256 = "4f4ee734b3c61a1a34e287d56b6c9021d9ab49d71e1357a7164369f509958463"
# avoid crash in raw thumbnailer
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
hardening = ["vis"]
# TODO
options = ["!cross"]
