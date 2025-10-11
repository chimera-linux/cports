pkgname = "timeshift"
pkgver = "25.07.7"
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
license = "GPL-2.0-or-later"
url = "https://projects.linuxmint.com/xapps"
source = (
    f"https://github.com/linuxmint/timeshift/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "c4de584ac4ab29d17edae35d372fc64fd3a92e6d15efb5eb8ea458b315c6d52f"
tool_flags = {"CFLAGS": ["-Wno-implicit-function-declaration"]}
hardening = ["vis"]
# FIXME lintpixmaps
options = ["!lintpixmaps"]
restricted = "FIXME: timeshift-gtk causes segmentation fault at strlen()"
