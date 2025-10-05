pkgname = "gst-libav"
pkgver = "1.26.6"
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
sha256 = "6e50a6222d509c52b19143f9a7bd3581e22c745d0c4bc27ddb07e1229bcc11b8"
# FIXME int
hardening = ["!int"]
