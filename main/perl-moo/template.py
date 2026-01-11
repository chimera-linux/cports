pkgname = "perl-moo"
pkgver = "2.005005"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = [
    "perl",
]
makedepends = ["perl"]
depends = [
    "perl-class-method-modifiers",
    "perl-role-tiny",
    "perl-sub-quote",
]
checkdepends = [*depends]
pkgdesc = "Moose-compatible object oriented library for perl"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/dist/Moo"
source = f"https://cpan.metacpan.org/authors/id/H/HA/HAARG/Moo-{pkgver}.tar.gz"
sha256 = "fb5a2952649faed07373f220b78004a9c6aba387739133740c1770e9b1f4b108"
