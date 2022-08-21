pkgname = "nspr"
pkgver = "4.34.1"
pkgrel = 0
build_wrksrc = "nspr"
build_style = "gnu_configure"
configure_args = ["--enable-optimize", "--enable-debug", "--enable-ipv6"]
make_cmd = "gmake"
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["zlib-devel"]
pkgdesc = "NetScape Portable Runtime"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MPL-2.0"
url = "https://www.mozilla.org/projects/nspr"
source = f"$(MOZILLA_SITE)/{pkgname}/releases/v{pkgver}/src/{pkgname}-{pkgver}.tar.gz"
sha256 = "c5b8354c48b632b8f4c1970628146c0e0c0ca8f32c7315d7d5736c002e03774f"
tool_flags = {
    "CFLAGS": [
        "-D_PR_POLL_AVAILABLE", "-D_PR_HAVE_OFF64_T", "-D_PR_INET6",
        "-D_PR_HAVE_INET_NTOP", "-D_PR_HAVE_GETHOSTBYNAME2",
        "-D_PR_HAVE_GETADDRINFO", "-D_PR_INET6_PROBE"
    ]
}
# no check target
options = ["!cross", "!check"]

if self.profile().wordsize == 64:
    configure_args += ["--enable-64bit"]

def post_install(self):
    self.rm(self.destdir / "usr/bin", recursive = True)
    self.rm(self.destdir / "usr/include/nspr/md", recursive = True)

@subpackage("nspr-devel")
def _devel(self):
    self.depends += [f"{pkgname}={pkgver}-r{pkgrel}"]

    # can't use default_devel, .so is not a symlink
    return [
        "usr/include",
        "usr/lib/pkgconfig",
        "usr/share/aclocal",
        "usr/lib/*.a",
    ]
