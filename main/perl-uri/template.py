pkgname = "perl-uri"
pkgver = "5.37"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl Uniform Resource Identifiers module"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/pod/URI"
source = f"$(CPAN_SITE)/URI/OALDERS/URI-{pkgver}.tar.gz"
sha256 = "5a8750ddd8ee743d7cc89bebdd542a9b78a34023164ebe19dea0c248e121c21e"
# missing checkdepends
options = ["!check"]
