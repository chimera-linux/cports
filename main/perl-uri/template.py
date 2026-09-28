pkgname = "perl-uri"
pkgver = "5.34"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl Uniform Resource Identifiers module"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/pod/URI"
source = f"$(CPAN_SITE)/URI/URI-{pkgver}.tar.gz"
sha256 = "de64c779a212ff1821896c5ca2bb69e74767d2674cee411e777deea7a22604a8"
# missing checkdepends
options = ["!check"]
