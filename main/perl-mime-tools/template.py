pkgname = "perl-mime-tools"
pkgver = "5.510"
pkgrel = 1
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
sha256 = "1bcfb4ece6ab4a6850ea1c8f3aa7405e233f50885dbdcd7bae546d52ec953cfe"
