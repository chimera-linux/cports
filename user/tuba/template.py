pkgname = "tuba"
pkgver = "0.10.0"
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
sha256 = "da86f8fcfbc8d47ca0c9e393827c7948594bddb90e475527db3e079b179870a6"
