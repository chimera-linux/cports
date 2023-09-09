pkgname = "perl-xml-parser"
pkgver = "2.46"
pkgrel = 1
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
sha256 = "d331332491c51cccfb4cb94ffc44f9cd73378e618498d4a37df9e043661c515d"
