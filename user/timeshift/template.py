pkgname = "timeshift"
pkgver = "24.06.6"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["gettext", "help2man", "meson", "pkgconf", "vala"]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "json-glib-devel",
    "libgee-devel",
    "vte-gtk3-devel",
    "xapp-devel",
]
depends = ["cronie", "psmisc", "rsync"]
pkgdesc = "System restore tool"
maintainer = "Earldridge Jazzed Pineda <earldridgejazzedpineda@gmail.com>"
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/xapps"
source = (
    f"https://github.com/linuxmint/timeshift/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "99123f5ee1792ae7d60e4d023e91ef04b9322fc271b5b90d18f6b1ecaa5188c2"
tool_flags = {"CFLAGS": ["-Wno-implicit-function-declaration"]}
hardening = ["vis"]
restricted = "FIXME: timeshift-gtk causes segmentation fault at strlen()"
