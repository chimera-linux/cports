pkgname = "guile"
pkgver = "3.0.10"
pkgrel = 0
build_style = "gnu_configure"
configure_args = [
    "--disable-error-on-warning",
    "--disable-lto",
    "--disable-static",
]
hostmakedepends = [
    "automake",
    "gettext-devel",
    "gperf",
    "libtool",
    "pkgconf",
]
makedepends = [
    "gc-devel",
    "gmp-devel",
    "libffi8-devel",
    "libunistring-devel",
    "ncurses-devel",
    "readline-devel",
]
pkgdesc = "GNU Scheme implementation"
maintainer = "Orphaned <orphaned@chimera-linux.org>"
license = "LGPL-3.0-or-later AND GPL-3.0-or-later"
url = "https://www.gnu.org/software/guile"
source = f"$(GNU_SITE)/guile/guile-{pkgver}.tar.gz"
sha256 = "2dbdbc97598b2faf31013564efb48e4fed44131d28e996c26abe8a5b23b56c2a"
# broken af
options = ["!lto"]


if self.profile().arch == "ppc":
    broken = "Pre-boot error; key: wrong-type-arg, args: ..."


@subpackage("guile-devel")
def _(self):
    self.depends += ["gc-devel", "gmp-devel"]
    return self.default_devel()
