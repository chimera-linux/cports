pkgname = "gst-libav"
pkgver = "1.24.2"
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
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "962838648e14ce8a78322ab16f84c7d84d86a6d7bebb6574ac05dea84a7c7c9b"
# FIXME int
hardening = ["!int"]
