pkgname = "dmg2img"
pkgver = "1.6.7"
pkgrel = 0
build_style = "makefile"
makedepends = ["bzip2-devel", "openssl3-devel", "zlib-ng-compat-devel"]
pkgdesc = "Compressed dmg to standard image disk file convert tool"
maintainer = "breakgimme <adam@plock.com>"
license = "GPL-2.0-only"
url = "http://vu1tur.eu.org/tools"
source = f"http://vu1tur.eu.org/tools/dmg2img-{pkgver}.tar.gz"
sha256 = "02aea6d05c5b810074913b954296ddffaa43497ed720ac0a671da4791ec4d018"
# no tests
options = ["!check"]
