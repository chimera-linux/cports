pkgname = "gst-libav"
pkgver = "1.22.10"
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
sha256 = "d6dda7aa38a44173278de675ccd92acff0abf473f7bc02e7d1cdd4ce0f3b7642"
# FIXME int
hardening = ["!int"]
