pkgname = "perl-glib"
pkgver = "1.3294"
pkgrel = 2
build_style = "perl_module"
hostmakedepends = [
    "perl",
    "perl-extutils-depends",
    "perl-extutils-pkgconfig",
]
makedepends = ["glib-devel", "perl"]
depends = ["perl"]
pkgdesc = "Perl module for GLib"
license = "LGPL-2.1-or-later"
url = "https://metacpan.org/dist/Glib"
source = f"$(CPAN_SITE)/Glib/Glib-{pkgver}.tar.gz"
sha256 = "d715f5a86bcc187075de85e7ae5bc07b0714d6edc196a92da43986efa44e5cbb"
