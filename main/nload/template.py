pkgname = "nload"
pkgver = "0.7.4"
pkgrel = 0
build_style = "gnu_configure"
make_dir = "."
hostmakedepends = ["automake"]
makedepends = ["ncurses-devel"]
pkgdesc = "Command line tool to visualize network traffic"
maintainer = "Iztok <iztok@iztok.space>"
license = "GPL-2.0-or-later"
url = "http://www.roland-riegel.de/nload"
source = f"$(SOURCEFORGE_SITE)/nload/nload/{pkgver}/{pkgname}-{pkgver}.tar.gz"
sha256 = "c1c051e7155e26243d569be5d99c744d8620e65fa8a7e05efcf84d01d9d469e5"
# no check target
options = ["!check"]
