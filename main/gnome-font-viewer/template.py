pkgname = "gnome-font-viewer"
pkgver = "44.0"
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
sha256 = "a1511df30b228cc2ef1175dd9d2b93438ea912e25913404b263cf3d457bb9f97"
# FIXME cfi
hardening = ["vis", "!cfi"]
