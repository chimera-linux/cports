pkgname = "gst-libav"
pkgver = "1.28.5"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "ffmpeg-devel",
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "orc-devel",
]
depends = ["orc", f"gst-plugins-base~{pkgver}"]
pkgdesc = "GStreamer FFmpeg plugin"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/gst-libav/gst-libav-{pkgver}.tar.xz"
sha256 = "452854656056f0b16511a1d9ad4f2679ff5e5a87c89f90cf7ee5dec005ddb1e4"
# FIXME int
hardening = ["!int"]
