pkgname = "gst-libav"
pkgver = "1.26.2"
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
sha256 = "2eceba9cae4c495bb4ea134c27f010356036f1fa1972db5f54833f5f6c9f8db0"
# FIXME int
hardening = ["!int"]
