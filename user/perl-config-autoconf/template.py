pkgname = "perl-config-autoconf"
pkgver = "0.320"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = [
    "perl",
    "perl-capture-tiny",
]
checkdepends = [*depends]
pkgdesc = "AutoConf macros implemented in Perl"
license = "Artistic-1.0-Perl"
url = "https://metacpan.org/pod/Config::AutoConf"
source = f"$(CPAN_SITE)/Config/Config-AutoConf-{pkgver}.tar.gz"
sha256 = "bb57a958ef49d3f7162276dae14a7bd5af43fd1d8513231af35d665459454023"
