pkgname = "meld"
pkgver = "3.24.1"
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
sha256 = "29dfee0d857b89c2fa4dad7c9fb9e48506d8bde3f71b6634798659e6697c6b1e"
