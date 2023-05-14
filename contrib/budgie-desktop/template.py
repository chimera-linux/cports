pkgname = "budgie-desktop"
pkgver = "10.7.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dwith-gtk-doc=false", "-Dwith-bluetooth=false", "-Dwith-gnome-screensaver=true"]
hostmakedepends = ["meson", "pkgconf", "intltool", "vala", "glib-devel", "gobject-introspection", "sassc", "budgie-screensaver"]
makedepends = [
    "alsa-lib-devel", "libcanberra-devel", "libgee-devel", "libnotify-devel", "accountsservice-devel", "libpeas-devel", "libwnck-devel", "mutter-devel", "ibus-devel", "gnome-desktop-devel", "libpulse-devel", "upower-devel", "gtk+3-devel", "polkit-devel", "gnome-menus-devel", "gnome-settings-daemon-devel", "vala", "upower-libs", "libuuid-devel"
]
pkgdesc = "Modern desktop environment from the Solus Project"
maintainer = "toukoAMG <toukoamg@tutanota.com>"
license = "GPL-2.0-only AND LGPL-2.1-only"
url = "https://github.com/BuddiesOfBudgie/budgie-desktop"
source = f"https://github.com/BuddiesOfBudgie/{pkgname}/releases/download/v{pkgver}/{pkgname}-v{pkgver}.tar.xz"
sha256 = "cce9ebe21b4bba4886bb2a227d739b7340c35085f08c132d3d8ae6b6621ba7b4"
# needs graphical environment
options = ["!check"]

@subpackage("budgie-desktop-devel")
def _devel(self):
    return self.default_devel()
