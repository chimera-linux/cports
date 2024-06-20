pkgname = "gstreamer-vaapi"
pkgver = "1.24.5"
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
sha256 = "fdb2da26b23895c56b20c6bad9edcf0faec3a3887765bc62c88f0955ed5b7c72"
