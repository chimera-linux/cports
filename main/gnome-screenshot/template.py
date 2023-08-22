pkgname = "gnome-screenshot"
pkgver = "41.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "gettext", "glib-devel"]
makedepends = [
    "libcanberra-devel",
    "glib-devel",
    "libhandy-devel",
    "gtk+3-devel",
    "libxext-devel",
    "libx11-devel",
]
pkgdesc = "Optional extensions for GNOME shell"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-screenshot"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "4adb7dec926428f74263d5796673cf142e4720b6e768f5468a8d0933f98c9597"
# FIXME cfi
hardening = ["vis", "!cfi"]
