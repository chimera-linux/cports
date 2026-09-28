pkgname = "gst-plugins-ugly"
pkgver = "1.28.7"
pkgrel = 1
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
sha256 = "2b681170ddc22b6b283cafeed48f427c30a17056974a6a9ed137c354e0f7730c"
