pkgname = "perl-mime-tools"
pkgver = "5.515"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = [
    "perl",
    "perl-convert-binhex",
    "perl-io-stringy",
    "perl-mailtools",
]
checkdepends = ["perl-test-deep"]
depends = [*makedepends]
pkgdesc = "Parses streams to create MIME entities"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/release/MIME-tools"
source = f"$(CPAN_SITE)/MIME/MIME-tools-{pkgver}.tar.gz"
sha256 = "c1ba1dd9f0b2cd82a0e75caedec51e48233f9f01dc29a0971bdff1cb53be9013"
