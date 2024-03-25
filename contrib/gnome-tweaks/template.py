pkgname = "gnome-tweaks"
pkgver = "46.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "gobject-introspection",
    "gtk-update-icon-cache",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "gsettings-desktop-schemas-devel",
    "gtk4-devel",
    "libadwaita-devel",
    "libgudev-devel",
    "python-gobject-devel",
]
depends = [
    "gnome-settings-daemon",
    "gnome-shell",
    "libadwaita",
    "python-gobject",
    "sound-theme-freedesktop",
]
pkgdesc = "GNOME tweak tool"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later AND CC0-1.0"
url = "https://wiki.gnome.org/Apps/Tweaks"
source = f"$(GNOME_SITE)/{pkgname}/{pkgver[:-2]}/{pkgname}-{pkgver}.tar.xz"
sha256 = "1678786341f664ac4580784222a16409fa9bf5cc7a5f1b46dcefd2aa13ddba31"
