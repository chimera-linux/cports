pkgname = "digikam"
pkgver = "8.5.0"
pkgrel = 2
build_style = "cmake"
configure_args = [
    "-DBUILD_TESTING=ON",
    "-DBUILD_WITH_QT6=ON",
    "-DQT_VERSION_MAJOR=6",
]
make_check_args = [
    "-j1",
    "-E",
    "("
    # hang
    + "databasesqliteinit|databaseswitch|haariface"
    # fail on ppc64le
    + "|(.*pgf.*)"
    # crashes/"not a qt plugin"
    + "|loadsavethread|dimg|setiptcpreview|timestampupdate|raw2dng)",
]
make_check_env = {"QT_QPA_PLATFORM": "offscreen"}
hostmakedepends = [
    "bison",
    "cmake",
    "extra-cmake-modules",
    "flex",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "akonadi-devel",
    "boost-devel",
    "eigen",
    "exiv2-devel",
    "ffmpeg-devel",
    "glib-devel",
    "jasper-devel",
    "kcalendarcore-devel",
    "ki18n-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "kservice-devel",
    "kwindowsystem-devel",
    "lcms2-devel",
    "lensfun-devel",
    "libexpat-devel",
    "libgphoto2-devel",
    "libheif-devel",
    "libjxl-devel",
    "libksane-devel",
    "libmagick-devel",
    "libomp-devel",
    "libpng-devel",
    "libtiff-devel",
    "libxml2-devel",
    "libxslt-devel",
    "opencv-devel",
    "qt6-qtbase-private-devel",  # qtx11extras_p.h
    "qt6-qtdeclarative-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtnetworkauth-devel",
    "qt6-qtscxml-devel",
    "qt6-qtsvg-devel",
    "qt6-qtwebengine-devel",
    "solid-devel",
    "sonnet-devel",
    "threadweaver-devel",
    "x265-devel",
]
depends = ["exiftool"]
checkdepends = [*depends]
pkgdesc = "Digital photo management application"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later AND GPL-2.0-or-later"
url = "https://www.digikam.org"
source = [
    f"$(KDE_SITE)/digikam/{pkgver}/digiKam-{pkgver}.tar.xz",
    "https://invent.kde.org/graphics/digikam-test-data/-/archive/d02dd20b23cc279792325a0f03d21688547a7a59.tar.gz",
]
source_paths = [".", "test-data"]
sha256 = [
    "5c4eaafbca59425a0fe8cb41e7d7a08446defbbb967528bb1148aed0e0d0e975",
    "fc4d21b83888016e6fb8f07bfc312bbdfa8fec8050d6df8b51475b43ab5fed91",
]
tool_flags = {
    "CFLAGS": ["-D_GNU_SOURCE"],
    "CXXFLAGS": ["-D_GNU_SOURCE"],
}
# a bunch of them fail with some mediawiki header check
options = ["!check"]


@subpackage("digikam-devel")
def _(self):
    return self.default_devel()
