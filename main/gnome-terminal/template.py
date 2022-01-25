pkgname = "gnome-terminal"
pkgver = "3.42.2"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dnautilus_extension=true", "-Db_ndebug=false",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "xsltproc",
    "docbook-xsl-nons", "itstool",
]
makedepends = [
    "gtk+3-devel", "vte3-devel", "dconf-devel", "libglib-devel", "pcre2-devel",
    "gsettings-desktop-schemas-devel", "libuuid-devel", "nautilus-devel",
    "gnome-shell",
]
pkgdesc = "GNOME terminal emulator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Terminal"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "8a9c8e5ef7a3a73b246a947e1190bb08ec98935af860cf0b3aa2fbf4606817a0"
options = ["!cross"]

@subpackage("nautilus-gnome-terminal-extension")
def _devel(self):
    self.pkgdesc = f"GNOME terminal extension for Nautilus"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "nautilus"]

    return ["usr/lib/nautilus"]
