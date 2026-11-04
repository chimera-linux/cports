pkgname = "gst-plugins-ugly"
pkgver = "1.28.8"
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
sha256 = "51ae53002e3bbe9ed0f2215020c5a248bf0ed41b9d9a2a4e102b8583fedab61c"
