pkgname = "gst-libav"
pkgver = "1.24.1"
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
sha256 = "549b7821fb5a4c866d6197888496015106cc6ec96ffb12a64e6efa91aa6562fd"
# FIXME int
hardening = ["!int"]
