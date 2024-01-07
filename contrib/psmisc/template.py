pkgname = "psmisc"
pkgver = "23.6"
pkgrel = 0
build_style = "gnu_configure"
make_cmd = "gmake"
hostmakedepends = ["gmake", "automake"]
makedepends = ["ncurses-devel", "gnu-getopt", "linux-headers"]
checkdepends = ["dejagnu"]
pkgdesc = "Small utilities that use the proc file-system"
maintainer = "roastveg <louis@hamptonsoftworks.com>"
license = "GPL-2.0-or-later"
url = "https://gitlab.com/psmisc/psmisc"
source = f"$(SOURCEFORGE_SITE)/{pkgname}/{pkgname}-{pkgver}.tar.xz"
sha256 = "257dde06159a4c49223d06f1cccbeb68933a4514fc8f1d77c64b54f0d108822a"
tool_flags = {
    "LDFLAGS": ["-lgnu_getopt"],
    "CFLAGS": ["-Dgetopt_long_only=gnu_getopt_long_only"],
}
hardening = ["vis", "cfi"]

configure_gen = []
