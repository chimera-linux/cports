pkgname = "perl-parallel-forkmanager"
pkgver = "2.03"
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
sha256 = "c0e0bead458224b9ac5bb32ed2b1fa088963b565521c1bb1a6a3566d522c2e35"
