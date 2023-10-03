pkgname = "gnome-calculator"
pkgver = "45.0.2"
pkgrel = 0
build_style = "meson"
# the library has some kind of weird meson issue:
# ERROR: Target 'gcalc-2' has 1 outputs: ['libgcalc-2.a'], but only 4 "install_dir"s were found
configure_args = ["-Dgcalc=false", "-Dgci=false"]
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
    "vala",
    "itstool",
    "gobject-introspection",
    "gtk-update-icon-cache",
    "desktop-file-utils",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "gtksourceview-devel",
    "libgee-devel",
    "mpc-devel",
    "libsoup-devel",
    "gsettings-desktop-schemas-devel",
]
depends = ["gsettings-desktop-schemas", "desktop-file-utils"]
pkgdesc = "GNOME calculator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Calculator"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-4]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "7dcbf32384897171cbe5483ec664d994e5e755e912ae1df911624f03c90867c2"

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
