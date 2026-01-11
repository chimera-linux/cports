pkgname = "perl-extutils-pkgconfig"
pkgver = "1.16"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = [
    "perl",
    "pkgconf",
]
makedepends = ["perl"]
depends = ["perl", "pkgconf"]
pkgdesc = "Perl module for pkg-config"
license = "LGPL-2.0-or-later"
url = "https://metacpan.org/pod/ExtUtils::PkgConfig"
source = f"$(CPAN_SITE)/ExtUtils/ExtUtils-PkgConfig-{pkgver}.tar.gz"
sha256 = "bbeaced995d7d8d10cfc51a3a5a66da41ceb2bc04fedcab50e10e6300e801c6e"
