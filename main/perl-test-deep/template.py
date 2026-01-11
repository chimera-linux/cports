pkgname = "perl-test-deep"
pkgver = "1.205"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Extremely flexible deep comparison"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/Test-Deep"
source = f"$(CPAN_SITE)/Test/Test-Deep-{pkgver}.tar.gz"
sha256 = "42781e9943a7a215e662c4973b9feafdc019fd16469bdb849a8537ee58956273"
# FIXME isa.t
options = ["!check"]
