pkgname = "cups-pk-helper"
pkgver = "0.2.7"
pkgrel = 1
build_style = "meson"
# XXX drop libexec
configure_args = ["--libexecdir=/usr/lib"]
hostmakedepends = ["meson", "pkgconf", "glib-devel", "gettext"]
makedepends = ["glib-devel", "cups-devel", "polkit-devel"]
pkgdesc = "PolicyKit helper to configure CUPS with fine-grained privileges"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.freedesktop.org/wiki/Software/cups-pk-helper"
source = f"https://gitlab.freedesktop.org/cups-pk-helper/cups-pk-helper/-/archive/{pkgver}/cups-pk-helper-{pkgver}.tar.gz"
sha256 = "8571a7d2fe459f340fc4031a374aced254305d09d96092c7951b90b1c493ab8d"
# needs cupsd running
options = ["!check"]
