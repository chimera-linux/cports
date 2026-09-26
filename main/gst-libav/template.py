pkgname = "gst-libav"
pkgver = "1.28.7"
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
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/gst-libav/gst-libav-{pkgver}.tar.xz"
sha256 = "58da51dd39ecf1cf6faade34cc6412001be2e2e145bca8ae0f45336f60a36ab2"
# FIXME int
hardening = ["!int"]
