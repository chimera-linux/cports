pkgname = "meld"
pkgver = "3.22.3"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "itstool",
    "libxml2-progs",
    "meson",
    "pkgconf",
]
makedepends = [
    "gtksourceview4-devel",
    "python-devel",
    "python-gobject-devel",
]
depends = [
    "gsettings-desktop-schemas",
    "gtksourceview4",
    "python-cairo",
    "python-gobject",
]
pkgdesc = "Visual diff and merge tool"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://meldmerge.org"
source = f"$(GNOME_SITE)/meld/{pkgver[:-2]}/meld-{pkgver}.tar.xz"
sha256 = "37f7f29eb1ff0fec4d8b088d5483c556de1089f6d018fe6d481993caf2499d84"
