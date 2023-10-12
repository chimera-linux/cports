pkgname = "shared-mime-info"
pkgver = "2.3"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dupdate-mimedb=false"]
hostmakedepends = ["meson", "pkgconf", "gettext", "xmlto", "libxml2-progs"]
makedepends = ["glib-devel", "libxml2-devel"]
triggers = ["/usr/share/mime"]
pkgdesc = "Core database of common types"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://freedesktop.org/wiki/Software/shared-mime-info"
source = f"https://gitlab.freedesktop.org/xdg/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "78eb7d0d6874e2116649067100d72e0d363eb6a51227797140dad3bd5643e6a9"
