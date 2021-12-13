pkgname = "shared-mime-info"
pkgver = "2.1"
pkgrel = 0
build_style = "meson"
configure_args = ["-Dupdate-mimedb=false"]
hostmakedepends = [
    "meson", "pkgconf", "gettext-tiny", "xmlto", "libxml2-progs"
]
makedepends = ["libglib-devel", "libxml2-devel"]
triggers = ["/usr/share/mime"]
pkgdesc = "Core database of common types"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://freedesktop.org/wiki/Software/shared-mime-info"
source = f"https://gitlab.freedesktop.org/xdg/{pkgname}/-/archive/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "3aeeee25ad445f257f614ed53837dee79fab70524b56e59b767f0d69e11fdff9"
