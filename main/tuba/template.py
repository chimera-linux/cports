pkgname = "tuba"
pkgver = "0.8.4"
pkgrel = 2
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
sha256 = "844fc1e3dc7d13a6967e9ac7c43bf887a00c9817f6666043ae002536d6a24c78"
