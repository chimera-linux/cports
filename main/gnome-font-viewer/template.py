pkgname = "gnome-font-viewer"
pkgver = "46.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "meson",
    "pkgconf",
    "glib-devel",
    "gettext",
]
makedepends = [
    "gtk4-devel",
    "libadwaita-devel",
    "glib-devel",
    "fontconfig-devel",
    "harfbuzz-devel",
    "freetype-devel",
    "gnome-desktop-devel",
]
pkgdesc = "Font viewer for GNOME"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-font-viewer"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "592f401e485d02cc044d487bb5c8e04c961da6856216768a59f1ff98bd2d537c"

tool_flags = {"CFLAGS": ["-Wno-incompatible-function-pointer-types"]}
