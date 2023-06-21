pkgname = "gst-libav"
pkgver = "1.22.4"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "gstreamer-devel",
    "gst-plugins-base-devel",
    "orc-devel",
    "ffmpeg-devel",
]
depends = ["orc", f"gst-plugins-base~{pkgver}"]
pkgdesc = "GStreamer FFmpeg plugin"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "9a751bc740de768e791c37a95f0a924c6a41d12fd7f37f54ce6a4e834be122d3"
# FIXME int
hardening = ["!int"]
