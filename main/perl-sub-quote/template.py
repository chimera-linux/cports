pkgname = "perl-sub-quote"
pkgver = "2.006009"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = [
    "perl",
]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module for eval-based subroutine generation"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/pod/Sub::Quote"
source = f"$(CPAN_SITE)/Sub/Sub-Quote-{pkgver}.tar.gz"
sha256 = "967282d54d2d51b198c67935594f93e4dea3e54d1e5bced158c94e29be868a4b"
