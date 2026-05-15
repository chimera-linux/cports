pkgname = "gst-plugins-ugly"
pkgver = "1.28.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--auto-features=enabled",
    "-Ddefault_library=shared",
    # missing deps
    "-Da52dec=disabled",
    "-Dmpeg2dec=disabled",
    "-Dsidplay=disabled",
    # not auto
    "-Dgpl=enabled",
    # misc
    "-Ddoc=disabled",
]
make_check_args = ["--timeout-multiplier=5"]
hostmakedepends = [
    "gettext",
    "meson",
    "orc",
    "pkgconf",
]
makedepends = [
    "gst-plugins-base-devel",
    "gstreamer-devel",
    "libcdio-devel",
    "libdvdread-devel",
    "x264-devel",
]
pkgdesc = "GStreamer ugly plugins"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/gst-plugins-ugly/gst-plugins-ugly-{pkgver}.tar.xz"
sha256 = "fe39a5ee7115e37de9eb65d899ec84c93e6e26ed3ffe25c6d5176cececbab572"
