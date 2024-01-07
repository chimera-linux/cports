pkgname = "gst-libav"
pkgver = "1.22.8"
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
sha256 = "be39349bc07ab4cdbd9a5fd6ea9848c601c7560ba5a0577ad5200b83bd424981"
# FIXME int
hardening = ["!int"]
