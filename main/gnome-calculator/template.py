pkgname = "gnome-calculator"
pkgver = "44.0"
pkgrel = 0
build_style = "meson"
# the library has some kind of weird meson issue:
# ERROR: Target 'gcalc-2' has 1 outputs: ['libgcalc-2.a'], but only 4 "install_dir"s were found
configure_args = ["-Dgcalc=false", "-Dgci=false"]
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny", "vala", "itstool",
    "gobject-introspection", "gtk-update-icon-cache", "desktop-file-utils",
]
makedepends = [
    "gtk4-devel", "libadwaita-devel", "gtksourceview-devel",
    "libgee-devel", "mpc-devel", "libsoup-devel",
    "gsettings-desktop-schemas-devel",
]
depends = ["gsettings-desktop-schemas", "desktop-file-utils"]
pkgdesc = "GNOME calculator"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://wiki.gnome.org/Apps/Calculator"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "14e763329f88309a7e152780d57361b543100e323906b34e0655fdc315b71043"

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
