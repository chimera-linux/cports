pkgname = "tuba"
pkgver = "0.8.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dclapper=true",
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
    "glib-devel",
    "gtksourceview-devel",
    "icu-devel",
    "json-glib-devel",
    "libadwaita-devel",
    "libgee-devel",
    "libsecret-devel",
    "libspelling-devel",
    "libxml2-devel",
]
depends = ["webp-pixbuf-loader"]
pkgdesc = "GTK fediverse client"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-3.0-or-later"
url = "https://tuba.geopjr.dev"
source = f"https://github.com/GeopJr/Tuba/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "b5791df008bc8ae7e1947cbd509b3bb905c4957c6dd65747676f85a4a2d3c3fe"
