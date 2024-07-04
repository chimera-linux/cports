pkgname = "gnome-terminal"
pkgver = "3.52.2"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "xsltproc",
    "docbook-xsl-nons",
    "itstool",
]
makedepends = [
    "glib-devel",
    "gsettings-desktop-schemas-devel",
    "gtk+3-devel",
    "libhandy-devel",
    "libuuid-devel",
    "nautilus-devel",
    "pcre2-devel",
    "vte-gtk3-devel",
]
pkgdesc = "GNOME terminal emulator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Terminal"
source = f"https://gitlab.gnome.org/GNOME/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "e4dbb694fcf5f15b6675c5dd9463d200bddf49e4ae42d0b3fbe87aef5829c930"
# Upstream claims "LTO very much NOT supported"
# https://gitlab.gnome.org/GNOME/gnome-terminal/-/blob/09c8b31168460c325ac00820759d6eefdf3957ab/meson.build#L226
options = ["!cross", "!lto"]


def post_install(self):
    self.uninstall("usr/lib/systemd")


@subpackage("nautilus-gnome-terminal-extension")
def _nautilus_extension(self):
    self.pkgdesc = "GNOME terminal extension for Nautilus"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "nautilus"]

    return [
        "usr/lib/nautilus",
        "usr/share/metainfo/org.gnome.Terminal.Nautilus.metainfo.xml",
    ]
