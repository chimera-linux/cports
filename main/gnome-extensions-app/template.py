pkgname = "gnome-extensions-app"
pkgver = "51_alpha"
pkgrel = 0
build_style = "meson"
configure_args = ["-Ddefault_library=shared"]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gjs",
    "gobject-introspection",
    "gtk+3-update-icon-cache",
    "meson",
    "pkgconf",
]
makedepends = ["libadwaita-devel"]
depends = ["gjs", "gnome-shell", "libadwaita"]
pkgdesc = "GNOME extensions manager"
license = "GPL-2.0-or-later"
url = "https://gitlab.gnome.org/GNOME/gnome-extensions-app"
source = f"$(GNOME_SITE)/gnome-extensions-app/{pkgver[0:2]}/gnome-extensions-app-{pkgver.replace('_', '.')}.tar.xz"
sha256 = "c60998fab1f67e73fcebeaa40c5806dc1ebffd6e1eb16e3b7472dc42691c85e6"
# introspection
options = ["!cross"]
