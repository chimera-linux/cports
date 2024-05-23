pkgname = "gnome-screenshot"
pkgver = "41.0"
pkgrel = 1
build_style = "meson"
hostmakedepends = ["gettext", "glib-devel", "meson", "pkgconf"]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "libcanberra-devel",
    "libhandy-devel",
    "libx11-devel",
    "libxext-devel",
]
pkgdesc = "GNOME screenshot utility"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-screenshot"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4adb7dec926428f74263d5796673cf142e4720b6e768f5468a8d0933f98c9597"
