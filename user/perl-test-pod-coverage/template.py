pkgname = "perl-test-pod-coverage"
pkgver = "1.10"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = ["perl"]
checkdepends = ["perl"]
pkgdesc = "Test::Pod::Coverage - Check for pod coverage in your distribution"
license = "Artistic-2.0"
url = "https://metacpan.org/dist/Test-Pod-Coverage"
source = f"$(CPAN_SITE)/Test/Test-Pod-Coverage-{pkgver}.tar.gz"
sha256 = "48c9cca9f7d99eee741176445b431adf09c029e1aa57c4703c9f46f7601d40d4"
# needs self for tests
options = ["!check"]
