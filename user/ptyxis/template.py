pkgname = "ptyxis"
pkgver = "50.1"
pkgrel = 0
build_style = "meson"
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "meson",
    "pkgconf",
]
makedepends = [
    "glib-devel",
    "json-glib-devel",
    "libadwaita-devel",
    "libportal-devel",
    "vte-gtk4-devel",
]
pkgdesc = "Terminal emulator for GNOME"
license = "GPL-3.0-only"
url = "https://gitlab.gnome.org/chergert/ptyxis"
source = f"https://gitlab.gnome.org/chergert/ptyxis/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "a4736088d1fbcb89e0bd63ad110edbeaaccd5220eaa680114945fe81e219a339"
