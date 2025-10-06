pkgname = "dconf-editor"
pkgver = "49.0"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "dconf-devel",
    "desktop-file-utils",
    "gettext",
    "glib-devel",
    "libhandy-devel",
    "meson",
    "pkgconf",
    "vala",
]
makedepends = [
    "dconf-devel",
    "glib-devel",
    "gtk+3-devel",
    "libhandy-devel",
]
pkgdesc = "Viewer and editor of applications internal dconf settings"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/dconf-editor"
source = f"$(GNOME_SITE)/dconf-editor/{pkgver[: -pkgver.rfind('.')]}/dconf-editor-{pkgver}.tar.xz"
sha256 = "90a8ccfadf51dff31e0028324fb9a358b2d26c5ae861a71c7dbf9f4dd9bdd399"
