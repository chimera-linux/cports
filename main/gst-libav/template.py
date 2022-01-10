pkgname = "gst-libav"
pkgver = "1.18.5"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = ["meson", "pkgconf"]
makedepends = [
    "gstreamer-devel", "gst-plugins-base-devel", "orc-devel", "ffmpeg-devel"
]
depends = ["orc", f"gst-plugins-base>={pkgver}"]
pkgdesc = "GStreamer FFmpeg plugin"
maintainer = "q66 <q66@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "822e008a910e9dd13aedbdd8dc63fedef4040c0ee2e927bab3112e9de693a548"
