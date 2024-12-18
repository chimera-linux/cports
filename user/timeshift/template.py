pkgname = "timeshift"
pkgver = "24.06.3"
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
sha256 = "d5151abba395ceb54d7b3383c52f30ed99ecb880d09c5a8c9f666dceef2015ca"
tool_flags = {"CFLAGS": ["-Wno-implicit-function-declaration"]}
hardening = ["vis"]
restricted = "FIXME: timeshift-gtk causes segmentation fault at strlen()"
