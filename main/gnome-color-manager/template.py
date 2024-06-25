pkgname = "gnome-color-manager"
pkgver = "3.36.0"
pkgrel = 1
build_style = "meson"
make_check_wrapper = ["wlheadless-run", "--"]
hostmakedepends = ["gettext", "glib-devel", "itstool", "meson", "pkgconf"]
makedepends = [
    "colord-devel",
    "glib-devel",
    "gtk+3-devel",
    "lcms2-devel",
    "libcanberra-devel",
]
depends = ["colord", "shared-color-targets"]
checkdepends = ["xwayland-run"]
pkgdesc = "Color profile manager for the GNOME desktop"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-color-manager"
source = f"$(GNOME_SITE)/gnome-color-manager/{pkgver[:-2]}/gnome-color-manager-{pkgver}.tar.xz"
sha256 = "9ddb9e6b6472e119801381f90905332ec1d4258981721bba831ca246ceb3ad3b"
