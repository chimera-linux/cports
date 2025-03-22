pkgname = "gnome-terminal"
pkgver = "3.56.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "docbook-xsl-nons",
    "gettext",
    "glib-devel",
    "itstool",
    "meson",
    "pkgconf",
    "libxslt-progs",
]
makedepends = [
    "glib-devel",
    "gsettings-desktop-schemas-devel",
    "gtk+3-devel",
    "libhandy-devel",
    "nautilus-devel",
    "pcre2-devel",
    "util-linux-uuid-devel",
    "vte-gtk3-devel",
]
pkgdesc = "GNOME terminal emulator"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Terminal"
source = f"https://gitlab.gnome.org/GNOME/gnome-terminal/-/archive/{pkgver}/gnome-terminal-{pkgver}.tar.gz"
sha256 = "aaa248152c62a51657367376d1c3262ce7c09d5c8321b30de63043a6de3720b1"
# Upstream claims "LTO very much NOT supported"
# https://gitlab.gnome.org/GNOME/gnome-terminal/-/blob/09c8b31168460c325ac00820759d6eefdf3957ab/meson.build#L226
options = ["!cross", "!lto"]


def post_install(self):
    self.uninstall("usr/lib/systemd")


@subpackage("gnome-terminal-nautilus-extension")
def _(self):
    self.pkgdesc = "GNOME terminal extension for Nautilus"
    self.depends += [self.parent]
    self.install_if = [self.parent, "nautilus"]
    # transitional
    self.provides = [self.with_pkgver("nautilus-gnome-terminal-extension")]

    return [
        "usr/lib/nautilus",
        "usr/share/metainfo/org.gnome.Terminal.Nautilus.metainfo.xml",
    ]
