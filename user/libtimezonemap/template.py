pkgname = "libtimezonemap"
pkgver = "0.4.6"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--enable-static"]
hostmakedepends = [
    "automake",
    "gobject-introspection",
    "libtool",
    "pkgconf",
]
makedepends = ["glib-devel", "gtk+3-devel", "json-glib-devel", "libsoup-devel"]
pkgdesc = "GTK+3 timezone map widget"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-3.0-or-later"
url = "https://launchpad.net/timezonemap"
source = f"$(DEBIAN_SITE)/main/libt/libtimezonemap/libtimezonemap_{pkgver}.orig.tar.gz"
sha256 = "0d634cc2476d8f57d1ee1864bd4f442180ae4bf040a9ae4bf73b66bbd85d7195"
options = ["!cross"]


@subpackage("libtimezonemap-devel")
def _(self):
    return self.default_devel()
