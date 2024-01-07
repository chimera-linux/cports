pkgname = "perl-test-deep"
pkgver = "1.204"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Extremely flexible deep comparison"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/Test-Deep"
source = f"$(CPAN_SITE)/Test/Test-Deep-{pkgver}.tar.gz"
sha256 = "b6591f6ccdd853c7efc9ff3c5756370403211cffe46047f082b1cd1611a84e5f"
# FIXME isa.t
options = ["!check"]
