pkgname = "cups-pk-helper"
pkgver = "0.2.6_git20210504"
# using git because last release was years ago and needs intltool
_commit = "151fbac90f62f959ccc648d4f73ca6aafc8f8e6a"
pkgrel = 0
build_style = "meson"
hostmakedepends = ["meson", "pkgconf", "glib-devel", "gettext-tiny"]
makedepends = ["libglib-devel", "cups-devel", "polkit-devel"]
pkgdesc = "PolicyKit helper to configure CUPS with fine-grained privileges"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/cups-pk-helper"
source = f"https://gitlab.freedesktop.org/{pkgname}/{pkgname}/-/archive/{_commit}.tar.gz"
sha256 = "5533c393dea1162cab4b946ceae838ea4d335e3b6ffb2cd8e2d0506e2294b7f9"
# needs cupsd running
options = ["!check"]
