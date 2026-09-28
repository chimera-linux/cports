pkgname = "ggrep"
pkgver = "3.12"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--program-prefix=g"]
# fails to regen due to gnulib junk
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["pcre2-devel"]
checkdepends = ["perl"]
pkgdesc = "GNU grep"
license = "GPL-3.0-or-later"
url = "https://www.gnu.org/software/grep"
source = f"$(GNU_SITE)/grep/grep-{pkgver}.tar.xz"
sha256 = "2649b27c0e90e632eadcd757be06c6e9a4f48d941de51e7c0f83ff76408a07b9"
hardening = ["vis", "cfi"]
