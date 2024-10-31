pkgname = "gstreamer-vaapi"
pkgver = "1.24.9"
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
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-or-later"
url = "https://gstreamer.freedesktop.org"
source = f"{url}/src/gstreamer-vaapi/gstreamer-vaapi-{pkgver}.tar.xz"
sha256 = "c2373e9b4d6655535d355207f60084b0fb3b28566fe9bb4ca1da714439da4ae1"
