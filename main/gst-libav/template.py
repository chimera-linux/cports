pkgname = "gst-libav"
pkgver = "1.20.3"
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
sha256 = "3fedd10560fcdfaa1b6462cbf79a38c4e7b57d7f390359393fc0cef6dbf27dfe"
