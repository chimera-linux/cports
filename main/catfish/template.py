pkgname = "catfish"
pkgver = "4.20.0"
pkgrel = 0
build_style = "meson"
_deps = ["python-dbus", "python-gobject", "python-pexpect"]
hostmakedepends = [
    "desktop-file-utils",
    "gettext",
    "meson",
    "pkgconf",
    *_deps,
]
makedepends = ["gtk+3-devel", "pango-devel", "xfconf-devel"]
depends = [
    "gtk+3",
    "pango",
    "cmd:locate!chimerautils-extra",
    "xfconf",
    *_deps,
]
pkgdesc = "Xfce file search tool"
maintainer = "triallax <triallax@tutanota.com>"
# TODO: https://gitlab.xfce.org/apps/catfish/-/issues/106
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/catfish/start"
source = f"$(XFCE_SITE)/apps/catfish/{pkgver[:-2]}/catfish-{pkgver}.tar.bz2"
sha256 = "3938a3cd5a9ecd75c9c7777f7204f8e4cfcb9960203ffd8c2df7d08d11a73a6e"
# No tests
options = ["!check"]
