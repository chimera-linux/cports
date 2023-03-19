pkgname = "gnome-terminal"
pkgver = "3.44.1"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dnautilus_extension=false", "-Db_ndebug=false",
]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "xsltproc",
    "docbook-xsl-nons", "itstool",
]
makedepends = [
    "gtk+3-devel", "vte-gtk3-devel", "dconf-devel", "libglib-devel",
    "pcre2-devel", "gsettings-desktop-schemas-devel", "libuuid-devel",
    "gnome-shell", #"nautilus-devel",
]
pkgdesc = "GNOME terminal emulator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://wiki.gnome.org/Apps/Terminal"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "fb6f20ee1ff231a9aaedab13d5dc6e5a64c955711224848b790086e88959d37b"
# FIXME cfi
hardening = ["vis", "!cfi"]
options = ["!cross"]

@subpackage("nautilus-gnome-terminal-extension", False)
def _devel(self):
    self.pkgdesc = f"GNOME terminal extension for Nautilus"
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.install_if = [f"{pkgname}={pkgver}-r{pkgrel}", "nautilus"]

    return ["usr/lib/nautilus"]
