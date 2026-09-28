pkgname = "perl-class-method-modifiers"
pkgver = "2.15"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = [
    "perl",
]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module for Moose-like method modifiers"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/pod/Class::Method::Modifiers"
source = f"$(CPAN_SITE)/Class/Class-Method-Modifiers-{pkgver}.tar.gz"
sha256 = "65cd85bfe475d066e9186f7a8cc636070985b30b0ebb1cde8681cf062c2e15fc"
