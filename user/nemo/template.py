pkgname = "nemo"
pkgver = "6.6.4"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dgtk_doc=true", "-Dtracker=true"]
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
license = "GPL-2.0-or-later AND GFDL-1.1-or-later AND LGPL-2.0-or-later"
url = "https://projects.linuxmint.com/cinnamon"
source = f"https://github.com/linuxmint/nemo/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "258807feb2e7bac523707d6b3daf2d9439e7135123cbe795183d5aaa6fd691ed"
# Tests require its own GSettings schemas to be installed
options = ["!check", "!cross"]


@subpackage("nemo-devel")
def _(self):
    return self.default_devel()
