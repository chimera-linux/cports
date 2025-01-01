pkgname = "tuba"
pkgver = "0.9.1"
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
    "gstreamer-devel",
    "gtksourceview-devel",
    "icu-devel",
    "json-glib-devel",
    "libadwaita-devel",
    "libgee-devel",
    "libsecret-devel",
    "libspelling-devel",
    "libxml2-devel",
]
depends = ["webp-pixbuf-loader", "gst-plugins-good"]
pkgdesc = "GTK fediverse client"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://tuba.geopjr.dev"
source = f"https://github.com/GeopJr/Tuba/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "1303e5e5646d73d6ef6c0b263a3f0ba72bf7573bea0d60f066e58f91a7bada1b"
