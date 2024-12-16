pkgname = "tuba"
pkgver = "0.9.0"
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
sha256 = "efdd74f543025473507b2f9b18e7c272c2376b779ff65f1a2f8e41f8b99fe2ac"
