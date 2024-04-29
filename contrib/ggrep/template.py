pkgname = "ggrep"
pkgver = "3.11"
pkgrel = 1
build_style = "gnu_configure"
configure_args = ["--program-prefix=g"]
hostmakedepends = ["automake", "libtool", "pkgconf", "gettext-devel"]
makedepends = ["pcre2-devel"]
checkdepends = ["perl"]
pkgdesc = "GNU grep"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/grep"
source = f"$(GNU_SITE)/grep/grep-{pkgver}.tar.xz"
sha256 = "1db2aedde89d0dea42b16d9528f894c8d15dae4e190b59aecc78f5a951276eab"
hardening = ["vis", "cfi"]
