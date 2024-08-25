pkgname = "nemo"
pkgver = "6.2.8"
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
    "libxml2-devel",
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
sha256 = "68d829614beeb2596aa706db5ff070fcfc0e96ab7e3d2561772b52bed6c8ca38"
# Tests require its own GSettings schemas to be installed
options = ["!check", "!cross"]


@subpackage("nemo-devel")
def _(self):
    return self.default_devel()
