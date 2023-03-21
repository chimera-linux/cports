pkgname = "shared-mime-info"
pkgver = "2.2"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dupdate-mimedb=false"]
hostmakedepends = [
    "meson", "pkgconf", "gettext-tiny", "xmlto", "libxml2-progs"
]
makedepends = ["glib-devel", "libxml2-devel"]
triggers = ["/usr/share/mime"]
pkgdesc = "Core database of common types"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://freedesktop.org/wiki/Software/shared-mime-info"
source = f"https://gitlab.freedesktop.org/xdg/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "bcf5d552318136cf7b3ae259975f414fbcdc9ebce000c87cf1f0901ff14e619f"
