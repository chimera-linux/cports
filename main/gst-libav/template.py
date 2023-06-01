pkgname = "gst-libav"
pkgver = "1.22.3"
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
sha256 = "2ec5c805808b4371a7e32b1da0202a1c8a6b36b6ce905080bf5c34097d12a923"
# FIXME int
hardening = ["!int"]
