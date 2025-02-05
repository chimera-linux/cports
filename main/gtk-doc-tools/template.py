pkgname = "gtk-doc-tools"
pkgver = "1.34.0"
pkgrel = 1
build_style = "meson"
# glib cyclic dep
configure_args = ["-Dtests=false"]
hostmakedepends = [
    "docbook-xml",
    "docbook-xsl-nons",
    "gettext",
    "itstool",
    "meson",
    "pkgconf",
    "python-pygments",
    "libxslt-progs",
]
depends = [
    "docbook-xml",
    "docbook-xsl-nons",
    "python-lxml",
    "python-pygments",
    "libxslt-progs",
]
pkgdesc = "Documentation tool for public library API"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND GFDL-1.1-or-later"
url = "http://www.gtk.org/gtk-doc"
source = f"$(GNOME_SITE)/gtk-doc/{pkgver[:-2]}/gtk-doc-{pkgver}.tar.xz"
sha256 = "b20b72b32a80bc18c7f975c9d4c16460c2276566a0b50f87d6852dff3aa7861c"
options = ["!splitdoc"]


def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/share/gtk-doc/python/gtkdoc")
