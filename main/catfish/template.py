pkgname = "catfish"
pkgver = "4.20.1"
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
    "cmd:locate!chimerautils-extra",
    "gtk+3",
    "pango",
    "xfconf",
    *_deps,
]
pkgdesc = "Xfce file search tool"
# TODO: https://gitlab.xfce.org/apps/catfish/-/issues/106
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/apps/catfish/start"
source = f"$(XFCE_SITE)/apps/catfish/{pkgver[:-2]}/catfish-{pkgver}.tar.xz"
sha256 = "fe00d45b163cf86b4c85ebdd23a73d53aa55bc97ba3f691a248ec403d4ade62b"
# No tests
options = ["!check"]
