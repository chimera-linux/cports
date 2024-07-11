pkgname = "gst-plugins-good-qt6"
pkgver = "1.24.5"
pkgrel = 0
build_style = "meson"
configure_args = [
    # qt6 only
    "--auto-features=disabled",
    "-Ddefault_library=shared",
    "-Dqt-egl=enabled",
    "-Dqt-wayland=enabled",
    "-Dqt-x11=enabled",
    "-Dqt6=enabled",
]
hostmakedepends = [
    "meson",
    "pkgconf",
    "qt6-qtbase",
    "qt6-qttools",
]
makedepends = [
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "qt6-qtbase-devel",
    "qt6-qtdeclarative-devel",
    "qt6-qttools-devel",
    "qt6-qtwayland-devel",
]
depends = [f"gst-plugins-good~{pkgver}"]
origin = "gst-plugins-good"
pkgdesc = "GStreamer good plugins"
subdesc = "Qt6 plugin"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/gst-plugins-good/gst-plugins-good-{pkgver}.tar.xz"
sha256 = "badcfc5292b035bde99a77327d468b2f0b116b40420bc9f25fb8e3970824ba75"
# FIXME int (extra tests fail, look for SIGILL) (in parent gst-plugins-good)
# in 1.24.4, pipelines_effectv only
hardening = ["!int"]
# no qt-specific tests, only examples
options = ["!check"]
