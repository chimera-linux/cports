pkgname = "whois"
pkgver = "5.6.3"
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
url = "https://github.com/rfc1036/whois"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5bdaf291465ef185384d9b5c4482f377a8040c008433b51d3cb8a4627f7aab14"
hardening = ["vis", "cfi"]
# no tests
options = ["!check"]

tool_flags = {
    "CFLAGS": ["-DHAVE_GETOPT_LONG", "-DHAVE_GETADDRINFO", "-DHAVE_SHA_CRYPT"]
}


def init_install(self):
    self.make_install_args.append(f"INSTALL_ROOT={self.chroot_destdir}")
