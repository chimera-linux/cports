pkgname = "perl-mime-tools"
pkgver = "5.514"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["gmake", "perl"]
makedepends = [
    "perl",
    "perl-convert-binhex",
    "perl-io-stringy",
    "perl-mailtools",
]
checkdepends = ["perl-test-deep"]
depends = list(makedepends)
pkgdesc = "Parses streams to create MIME entities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/MIME-tools"
source = f"$(CPAN_SITE)/MIME/MIME-tools-{pkgver}.tar.gz"
sha256 = "e13df8950c5ad4cb5f3f85fceb39dd21957287ef9f36c227ea0c86591795fee8"
