pkgname = "gst-plugins-ugly"
pkgver = "1.24.10"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/gst-plugins-ugly/gst-plugins-ugly-{pkgver}.tar.xz"
sha256 = "9df6fd85a7256241efbb25f84b337575e3b345266f5dab3849371e4694779f18"
