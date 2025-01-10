pkgname = "gstreamer-vaapi"
pkgver = "1.24.11"
pkgrel = 0
build_style = "meson"
configure_args = [
    "--auto-features=enabled",
    "-Ddefault_library=shared",
    # misc
    "-Ddoc=disabled",
]
make_check_args = ["--timeout-multiplier=5"]
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
    "wayland-progs",
]
makedepends = [
    "gstreamer-devel",
    "gst-plugins-bad-devel",
    "gst-plugins-base-devel",
    "gtk+3-devel",
    "libva-devel",
    "libxrandr-devel",
    "wayland-protocols",
]
pkgdesc = "GStreamer VA-API plugins"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/gstreamer-vaapi/gstreamer-vaapi-{pkgver}.tar.xz"
sha256 = "e85904a47d9ecb41d7f76b1d3fe887fa18c0b81a3793e7d7f61361ea7e90420d"
