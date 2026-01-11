pkgname = "pcsc-perl"
pkgver = "1.4.16"
pkgrel = 2
build_style = "perl_module"
hostmakedepends = ["perl", "pkgconf"]
makedepends = ["pcsc-lite-devel", "perl"]
pkgdesc = "Perl module for PCSC"
license = "GPL-2.0-or-later"
url = "https://pcsc-perl.apdu.fr"
source = f"https://github.com/LudovicRousseau/pcsc-perl/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8fd21f975e6a453a8461896e1700ce6d20092341e1d8946e833c134b092856df"
# check: requires real pcsc
# cross: fails to add pcsc incdir
options = ["!check", "!cross"]
