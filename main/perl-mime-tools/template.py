pkgname = "perl-mime-tools"
pkgver = "5.512"
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
sha256 = "05a76bb173ba3971d1186981978033ca4631ebce17d44e564db8c8dba34ae99a"
