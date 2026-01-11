pkgname = "perl-regexp-common"
pkgver = "2024080801"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
checkdepends = ["perl"]
depends = ["perl"]
pkgdesc = "Provide commonly requested regular expressions"
license = "Artistic-1.0-Perl OR Artistic-2.0 OR MIT OR BSD-2-Clause"
url = "https://metacpan.org/pod/Regexp::Common"
source = f"$(CPAN_SITE)/Regexp/Regexp-Common-{pkgver}.tar.gz"
sha256 = "0677afaec8e1300cefe246b4d809e75cdf55e2cc0f77c486d13073b69ab4fbdd"


def post_install(self):
    self.install_license("COPYRIGHT.BSD")
    self.install_license("COPYRIGHT.MIT")
