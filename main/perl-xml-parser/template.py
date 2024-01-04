pkgname = "perl-xml-parser"
pkgver = "2.47"
pkgrel = 0
build_style = "perl_module"
make_build_args = ["MAKE=gmake"]
make_install_args = ["MAKE=gmake"]
make_check_args = ["MAKE=gmake"]
hostmakedepends = ["gmake", "perl"]
makedepends = ["perl", "libexpat-devel"]
depends = ["perl"]
pkgdesc = "Perl interface to libexpat"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/XML-Parser"
source = f"$(CPAN_SITE)/XML/XML-Parser-{pkgver}.tar.gz"
sha256 = "ad4aae643ec784f489b956abe952432871a622d4e2b5c619e8855accbfc4d1d8"
