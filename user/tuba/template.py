pkgname = "tuba"
pkgver = "0.10.3"
pkgrel = 1
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
sha256 = "397297bbd140a2b2c90024392dbc5f8a77bc6a10472308c7741c7913e82eb050"
