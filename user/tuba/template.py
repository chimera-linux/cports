pkgname = "tuba"
pkgver = "0.10.2"
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
depends = ["webp-pixbuf-loader", "gst-plugins-good"]
pkgdesc = "GTK fediverse client"
license = "GPL-3.0-or-later"
url = "https://tuba.geopjr.dev"
source = f"https://github.com/GeopJr/Tuba/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "2adc7921ede1d6d1a8b3e6395e12235e8acbe5d9a1957e9419317101bd1c5b8a"
