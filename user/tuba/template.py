pkgname = "tuba"
pkgver = "0.11.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Ddistro=true",
]
hostmakedepends = [
    "gettext",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "clapper-devel",
    "gexiv2-devel",
    "glib-devel",
    "gstreamer-devel",
    "gtksourceview-devel",
    "icu-devel",
    "json-glib-devel",
    "libadwaita-devel",
    "libgee-devel",
    "libsecret-devel",
    "libspelling-devel",
    "libxml2-devel",
    "webkitgtk4-devel",
]
depends = ["gst-plugins-good"]
pkgdesc = "GTK fediverse client"
license = "GPL-3.0-or-later"
url = "https://tuba.geopjr.dev"
source = f"https://github.com/GeopJr/Tuba/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "10de8fab3dbd1e7d3f6482060e007cceaaa81f88aebd7a9e44e6e677608414eb"
