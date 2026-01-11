pkgname = "razor"
pkgver = "2.86"
pkgrel = 2
build_style = "perl_module"
hostmakedepends = [
    "perl",
]
makedepends = ["perl"]
depends = ["perl", "perl-uri"]
pkgdesc = "Distributed, collaborative spam detection and filtering network"
license = "Artistic-2.0"
url = "https://sourceforge.net/projects/razor"
source = f"https://cpan.metacpan.org/authors/id/T/TO/TODDR/Razor2-Client-Agent-{pkgver}.tar.gz"
sha256 = "5e062e02ebb65e24b708e7eefa5300c43d6f657bf20d08fec4ca8a0a3b94845f"
