pkgname = "shared-mime-info"
pkgver = "2.4"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dupdate-mimedb=false"]
hostmakedepends = ["meson", "pkgconf", "gettext", "xmlto", "libxml2-progs"]
makedepends = ["glib-devel", "libxml2-devel"]
triggers = ["/usr/share/mime"]
pkgdesc = "Core database of common types"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://freedesktop.org/wiki/Software/shared-mime-info"
source = f"https://gitlab.freedesktop.org/xdg/shared-mime-info/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "531291d0387eb94e16e775d7e73788d06d2b2fdd8cd2ac6b6b15287593b6a2de"
