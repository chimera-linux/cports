pkgname = "gst-libav"
pkgver = "1.26.1"
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
sha256 = "350a20b45b6655b6e10265430bdfbb3c436a96e9611b79caabef8f10abe570ea"
# FIXME int
hardening = ["!int"]
