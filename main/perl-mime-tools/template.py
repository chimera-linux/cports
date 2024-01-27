pkgname = "perl-mime-tools"
pkgver = "5.513"
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
sha256 = "48d81841bcd45d5565c17f761ab0f730b4dc71e91a17959446503ce6b7e2da9c"
