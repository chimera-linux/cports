pkgname = "perl-uri"
pkgver = "5.36"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl Uniform Resource Identifiers module"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/pod/URI"
source = (
    f"https://cpan.metacpan.org/authors/id/O/OA/OALDERS/URI-{pkgver}.tar.gz"
)
sha256 = "32719e57413db6e18492e104707b95c2210df637614c512e7368c9ec3c2f783b"
# missing checkdepends
options = ["!check"]
