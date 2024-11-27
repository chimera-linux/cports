pkgname = "meld"
pkgver = "3.22.2"
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
sha256 = "46a0a713fbcd1b153b377a1e0757c8ce255c9822467658eacfbd89b1e92316ef"
