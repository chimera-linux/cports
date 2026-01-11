pkgname = "perl-uri"
pkgver = "5.32"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl Uniform Resource Identifiers module"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/pod/URI"
source = f"$(CPAN_SITE)/URI/URI-{pkgver}.tar.gz"
sha256 = "9632067d34e14e0dae2da94631c4f25a387fcc48d06fa29330e8b3c04c4e913d"
# missing checkdepends
options = ["!check"]
