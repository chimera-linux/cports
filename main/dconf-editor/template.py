pkgname = "dconf-editor"
pkgver = "45.0.1"
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
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://gitlab.gnome.org/GNOME/dconf-editor"
source = f"$(GNOME_SITE)/dconf-editor/{pkgver[: -pkgver.rfind('.')]}/dconf-editor-{pkgver}.tar.xz"
sha256 = "1180297678eedae6217cc514a2638c187d2f1d1ef2720cb9079b740c429941dd"
