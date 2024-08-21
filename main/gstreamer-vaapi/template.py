pkgname = "gstreamer-vaapi"
pkgver = "1.24.7"
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
sha256 = "3aa5ed9d7f4b5a7cb60d8b0370d983d59395de546ee76704401180fd0fd5ee86"
