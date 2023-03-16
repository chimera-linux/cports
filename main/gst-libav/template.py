pkgname = "gst-libav"
pkgver = "1.22.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "gstreamer-devel", "gst-plugins-base-devel", "orc-devel", "ffmpeg-devel"
]
depends = ["orc", f"gst-plugins-base~{pkgver}"]
pkgdesc = "GStreamer FFmpeg plugin"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "c958e825dc3ac3b7a481f8db5268131a1cd701312385c2d803dc63c8e460b5fb"
# FIXME int
hardening = ["!int"]
