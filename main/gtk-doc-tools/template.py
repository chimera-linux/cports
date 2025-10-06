pkgname = "gtk-doc-tools"
pkgver = "1.35.1"
pkgrel = 0
build_style = "meson"
# glib cyclic dep
configure_args = ["-Dtests=false"]
hostmakedepends = [
    "docbook-xml",
    "docbook-xsl-nons",
    "gettext",
    "itstool",
    "libxslt-progs",
    "meson",
    "pkgconf",
    "python-pygments",
]
depends = [
    "docbook-xml",
    "docbook-xsl-nons",
    "libxslt-progs",
    "python-lxml",
    "python-pygments",
]
pkgdesc = "Documentation tool for public library API"
license = "GPL-2.0-or-later AND GFDL-1.1-or-later"
url = "http://www.gtk.org/gtk-doc"
source = f"$(GNOME_SITE)/gtk-doc/{pkgver[:-2]}/gtk-doc-{pkgver}.tar.xz"
sha256 = "611c9f24edd6d88a8ae9a79d73ab0dc63c89b81e90ecc31d6b9005c5f05b25e2"
options = ["!splitdoc"]


def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/share/gtk-doc/python/gtkdoc")
