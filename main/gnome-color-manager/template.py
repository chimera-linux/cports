pkgname = "gnome-color-manager"
pkgver = "3.36.2"
pkgrel = 0
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
sha256 = "3904d42abb4ea566df0b880e82bf0b9f86386c692f15b318469a4c7be33a887f"
