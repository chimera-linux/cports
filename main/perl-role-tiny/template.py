pkgname = "perl-role-tiny"
pkgver = "2.002004"
pkgrel = 1
build_style = "perl_module"
hostmakedepends = [
    "perl",
]
makedepends = ["perl"]
depends = ["perl"]
pkgdesc = "Perl module for role composition"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/pod/Role::Tiny"
source = (
    f"https://cpan.metacpan.org/authors/id/H/HA/HAARG/Role-Tiny-{pkgver}.tar.gz"
)
sha256 = "d7bdee9e138a4f83aa52d0a981625644bda87ff16642dfa845dcb44d9a242b45"
