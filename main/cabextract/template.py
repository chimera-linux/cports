pkgname = "cabextract"
pkgver = "1.11"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--with-external-libmspack"]
# broken
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["libmspack-devel"]
pkgdesc = "Tool for extracting Microsoft cabinet files"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "GPL-2.0-or-later"
url = "https://www.cabextract.org.uk"
source = f"https://www.cabextract.org.uk/cabextract-{pkgver}.tar.gz"
sha256 = "b5546db1155e4c718ff3d4b278573604f30dd64c3c5bfd4657cd089b823a3ac6"
hardening = ["vis", "!cfi"]
