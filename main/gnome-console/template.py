pkgname = "gnome-console"
pkgver = "44_beta1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny",
    "gobject-introspection", "gtk-update-icon-cache",
    "desktop-file-utils",
]
makedepends = [
    "gtk4-devel", "libadwaita-devel", "vte-gtk4-devel",
    "libgtop-devel", "gsettings-desktop-schemas-devel",
    "pcre2-devel",
]
pkgdesc = "GNOME console"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/console"
source = f"$(GNOME_SITE)/{pkgname}/44/{pkgname}-44.beta.tar.xz"
sha256 = "92633f31f936fa4bc18e26fc25077830e12962fb72edd5c1fa75f5fe834b92ee"
