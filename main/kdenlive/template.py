pkgname = "kdenlive"
pkgver = "25.04.0"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DBUILD_TESTING=OFF", "-DFETCH_OTIO=OFF"]
hostmakedepends = [
    "cmake",
    "extra-cmake-modules",
    "gettext",
    "ninja",
    "pkgconf",
]
makedepends = [
    "ffmpeg-devel",
    "imath-devel",
    "karchive-devel",
    "kbookmarks-devel",
    "kcodecs-devel",
    "kconfig-devel",
    "kconfigwidgets-devel",
    "kcoreaddons-devel",
    "kcrash-devel",
    "kdbusaddons-devel",
    "kdoctools-devel",
    "kfilemetadata-devel",
    "kguiaddons-devel",
    "kiconthemes-devel",
    "kio-devel",
    "knewstuff-devel",
    "knotifications-devel",
    "knotifyconfig-devel",
    "ktextwidgets-devel",
    "kwidgetsaddons-devel",
    "kxmlgui-devel",
    "mlt-devel",
    "opentimelineio-devel",
    "purpose-devel",
    "qt6-qtmultimedia-devel",
    "qt6-qtnetworkauth-devel",
    "qt6-qtsvg-devel",
    "solid-devel",
    "v4l-utils-devel",
]
depends = [
    "ffmpeg",
    "frei0r",
]
pkgdesc = "KDE video editor"
license = "GPL-2.0-or-later"
url = "https://apps.kde.org/kdenlive"
source = f"$(KDE_SITE)/release-service/{pkgver}/src/kdenlive-{pkgver}.tar.xz"
sha256 = "3f07e23e5e58441acd02b89d969b33940994d9d1a8a8006b15e61eb575abd519"
# avoid crashes
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# INT: crashes spacertest/trimmingtest
hardening = ["vis", "!int"]
# TODO
# check: takes forever to build + sometimes hangs etc
options = ["!cross", "!check"]
