pkgname = "perl-parallel-forkmanager"
pkgver = "2.04"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl-moo"]
checkdepends = [
    "perl-test-warn",
    *depends,
]
pkgdesc = "Parallel processing fork manager"
license = "Artistic-1.0-Perl"
url = "https://metacpan.org/pod/Parallel::ForkManager"
source = f"$(CPAN_SITE)/Parallel/Parallel-ForkManager-{pkgver}.tar.gz"
sha256 = "606894fc2e9f7cd13d9ec099aaac103a8f0943d1d80c2c486bae14730a39b7fc"
