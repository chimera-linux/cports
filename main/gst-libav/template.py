pkgname = "gst-libav"
pkgver = "1.24.4"
pkgrel = 1
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
sha256 = "4d3803f36008e847fc4842c8dd366162baf8359526cc46c1851bf68bb638da73"
# FIXME int
hardening = ["!int"]
