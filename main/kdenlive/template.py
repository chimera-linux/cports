pkgname = "kdenlive"
pkgver = "25.12.1"
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
sha256 = "ab40da31896a1e0931e6acd59820082c0e10cc5efc599d40025fc0a0eb8039c0"
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
