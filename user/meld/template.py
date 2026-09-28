pkgname = "meld"
pkgver = "3.24.0"
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
license = "GPL-2.0-or-later"
url = "https://meldmerge.org"
source = f"$(GNOME_SITE)/meld/{pkgver[:-2]}/meld-{pkgver}.tar.xz"
sha256 = "19f036297e7c89514516bcd2e56182db2bb2ba13b4850893c1ce597445018b94"
