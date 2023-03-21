pkgname = "gnome-font-viewer"
pkgver = "43.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson", "pkgconf", "glib-devel", "gettext-tiny",
]
makedepends = [
    "gtk4-devel", "libadwaita-devel", "glib-devel", "fontconfig-devel",
    "harfbuzz-devel", "freetype-devel", "gnome-desktop-devel",
]
pkgdesc = "Font viewer for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-font-viewer"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "81c6bffb06d5332346e00eaecaec1bdcfd617c51dfd95bcd058d6c76c76dd2b9"
# FIXME cfi
hardening = ["vis", "!cfi"]
