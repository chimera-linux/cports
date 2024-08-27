pkgname = "tuba"
pkgver = "0.8.3"
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
sha256 = "6c2fce949ac4d102f07ebcb94eb39ebb85309032c07f9eda88386dc8e10f9636"
