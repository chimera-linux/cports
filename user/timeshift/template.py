pkgname = "timeshift"
pkgver = "24.06.5"
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
sha256 = "237c1b901c5ba1e72ffdf1779d52077229a5902f79c03548342eac3b22a62ec4"
tool_flags = {"CFLAGS": ["-Wno-implicit-function-declaration"]}
hardening = ["vis"]
restricted = "FIXME: timeshift-gtk causes segmentation fault at strlen()"
