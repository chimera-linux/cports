pkgname = "gtk-doc-tools"
pkgver = "1.33.2"
pkgrel = 2
build_style = "meson"
# glib cyclic dep
configure_args = ["-Dtests=false"]
hostmakedepends = [
    "meson",
    "docbook-xml",
    "docbook-xsl-nons",
    "itstool",
    "xsltproc",
    "pkgconf",
    "python-pygments",
    "gettext",
]
depends = [
    "docbook-xml",
    "docbook-xsl-nons",
    "xsltproc",
    "python-pygments",
    "python-lxml",
]
pkgdesc = "Documentation tool for public library API"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later AND GFDL-1.1-or-later"
url = "http://www.gtk.org/gtk-doc"
source = f"$(GNOME_SITE)/gtk-doc/{pkgver[:-2]}/gtk-doc-{pkgver}.tar.xz"
sha256 = "cc1b709a20eb030a278a1f9842a362e00402b7f834ae1df4c1998a723152bf43"
options = ["!splitdoc"]


def post_install(self):
    from cbuild.util import python

    python.precompile(self, "usr/share/gtk-doc/python/gtkdoc")
