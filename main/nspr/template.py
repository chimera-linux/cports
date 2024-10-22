pkgname = "nspr"
pkgver = "4.36"
pkgrel = 0
build_wrksrc = "nspr"
build_style = "gnu_configure"
configure_args = ["--enable-optimize", "--enable-debug", "--enable-ipv6"]
configure_gen = []
hostmakedepends = ["pkgconf"]
makedepends = ["zlib-ng-compat-devel"]
pkgdesc = "NetScape Portable Runtime"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://www.mozilla.org/projects/nspr"
source = f"$(MOZILLA_SITE)/nspr/releases/v{pkgver}/src/nspr-{pkgver}.tar.gz"
sha256 = "55dec317f1401cd2e5dba844d340b930ab7547f818179a4002bce62e6f1c6895"
tool_flags = {
    "CFLAGS": [
        "-D_PR_POLL_AVAILABLE",
        "-D_PR_HAVE_OFF64_T",
        "-D_PR_INET6",
        "-D_PR_HAVE_INET_NTOP",
        "-D_PR_HAVE_GETHOSTBYNAME2",
        "-D_PR_HAVE_GETADDRINFO",
        "-D_PR_INET6_PROBE",
    ]
}
# CFI: crashes nss build
hardening = ["vis", "!cfi"]
# no check target
options = ["!cross", "!check"]

if self.profile().wordsize == 64:
    configure_args += ["--enable-64bit"]


def post_install(self):
    self.uninstall("usr/bin")
    self.uninstall("usr/include/nspr/md")


@subpackage("nspr-devel")
def _(self):
    self.depends += [self.parent]
    return self.default_devel()
