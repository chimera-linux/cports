pkgname = "whois"
pkgver = "5.6.4"
pkgrel = 0
build_style = "makefile"
make_build_args = [
    "CONFIG_FILE=/etc/whois.conf",
    "HAVE_ICONV=1",
]
make_install_target = "install-whois"
make_install_args = ["install-mkpasswd"]
hostmakedepends = [
    "gettext",
    "perl",
    "pkgconf",
]
makedepends = [
    "libidn2-devel",
]
pkgdesc = "Intelligent WHOIS Client"
license = "GPL-2.0-or-later"
url = "https://salsa.debian.org/md/whois"
source = f"{url}/-/archive/v{pkgver}/whois-v{pkgver}.tar.gz"
sha256 = "bb5bc6a5c2e727fc81e75691acb0d7a771cf3149448feffa331755316a0f7034"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]

tool_flags = {
    "CFLAGS": ["-DHAVE_GETOPT_LONG", "-DHAVE_GETADDRINFO", "-DHAVE_SHA_CRYPT"]
}


def init_install(self):
    self.make_install_args.append(f"INSTALL_ROOT={self.chroot_destdir}")
