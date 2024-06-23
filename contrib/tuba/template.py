pkgname = "tuba"
pkgver = "0.8.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    # change this on next clapper update- current version mostly crashes after
    # closing the player
    "-Dclapper=false",
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
sha256 = "2c52448061bc82e2a7690faa2bd16e1d3cb506bd0b1a2b1ed32623051710ba06"
