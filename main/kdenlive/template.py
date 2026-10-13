pkgname = "kdenlive"
pkgver = "26.08.2"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-DBUILD_TESTING=OFF",
    # fails badly (11f33a8194bea7fbe2f4c73c13df3ab120bc8752)
    "-DBUILD_RUN_QMLLINT=OFF",
    "-DFETCH_OTIO=OFF",
]
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
    "kddockwidgets-devel",
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
sha256 = "1019cda23429a526e3a2dbdd2ec93406fef0c89ca243af16dfa16ac9ae8a6bf8"
# avoid crashes
tool_flags = {"LDFLAGS": ["-Wl,-z,stack-size=0x200000"]}
# INT: crashes spacertest/trimmingtest
hardening = ["vis", "!int"]
# TODO
# check: takes forever to build + sometimes hangs etc
options = ["!cross", "!check"]


def post_install(self):
    # unused post-build artifact of kdenliveLib's ecm_add_qml_module()
    self.uninstall("usr/lib/libkdenliveLibplugin.a")
