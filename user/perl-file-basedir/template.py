pkgname = "perl-file-basedir"
pkgver = "0.09"
pkgrel = 0
build_style = "perl_module"
hostmakedepends = ["perl"]
makedepends = ["perl"]
depends = [
    "perl-file-which",
    "perl-ipc-system-simple",
]
checkdepends = [*depends]
pkgdesc = "Parses streams to create MIME entities"
license = "Artistic-1.0-Perl OR GPL-1.0-or-later"
url = "https://metacpan.org/dist/File-BaseDir"
source = f"$(CPAN_SITE)/File/File-BaseDir-{pkgver}.tar.gz"
sha256 = "6da6f7281562ac8f11ef1a3af6aedb51c41182b60f1f122ced0079efd92967d9"
