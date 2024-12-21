pkgname = "nemo"
pkgver = "6.4.3"
pkgrel = 0
build_style = "meson"
# XXX: drop libexec
configure_args = ["--libexecdir=/usr/lib", "-Dgtk_doc=true", "-Dtracker=true"]
hostmakedepends = [
    "gobject-introspection",
    "gtk-doc-tools",
    "intltool",
    "meson",
    "pkgconf",
]
makedepends = [
    "cinnamon-desktop-devel",
    "exempi-devel",
    "glib-devel",
    "gtk+3-devel",
    "json-glib-devel",
    "libexif-devel",
    "libgsf-devel",
    "libx11-devel",
    "pango-devel",
    "tinysparql-devel",
    "xapp-devel",
]
depends = [
    "gtk+3",
    "pango>=1.54.0-r3",  # Requires pango without "int" hardening
    "python-cairo",
    "python-gobject",
    "xapp",
]
pkgdesc = "File browser for Cinnamon"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-2.0-or-later AND GFDL-1.1-or-later AND LGPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/nemo/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "dc4b2ed52fd69551a53fd95a008a738fc9c904fc79d41c8e39ec49bfd739094e"
# Tests require its own GSettings schemas to be installed
options = ["!check", "!cross"]


@subpackage("nemo-devel")
def _(self):
    return self.default_devel()
