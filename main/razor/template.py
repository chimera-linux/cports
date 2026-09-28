pkgname = "razor"
pkgver = "2.88"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = [
    "perl",
]
makedepends = ["perl"]
depends = ["perl", "perl-uri"]
checkdepends = ["perl-uri"]
pkgdesc = "Distributed, collaborative spam detection and filtering network"
license = "Artistic-2.0"
url = "https://sourceforge.net/projects/razor"
source = f"https://cpan.metacpan.org/authors/id/T/TO/TODDR/Razor2-Client-Agent-{pkgver}.tar.gz"
sha256 = "1586f1ef8759d6d52de9b1cd43056c3866161f8fd0db0048b25d46473658fdaa"
