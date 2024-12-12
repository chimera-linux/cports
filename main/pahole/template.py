pkgname = "pahole"
pkgver = "1.28"
pkgrel = 0
build_style = "cmake"
configure_args = [
    "-D__LIB=lib",
    "-DLIBBPF_EMBEDDED=OFF",
]
hostmakedepends = [
    "cmake",
    "ninja",
    "pkgconf",
]
makedepends = [
    "argp-standalone",
    "elfutils-devel",
    "libbpf-devel",
    "linux-headers",
    "musl-obstack-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Debug information utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://git.kernel.org/pub/scm/devel/pahole/pahole.git"
source = f"https://fedorapeople.org/~acme/dwarves/dwarves-{pkgver}.tar.xz"
sha256 = "a4c1a3c16c7d41f27eba8323e05b59fe33581832d5c50ef8390fa102d75a16e3"
tool_flags = {
    # see libbpf comment about bpf headers
    "CFLAGS": ["-I/usr/include/bpf/uapi"],
    "CXXFLAGS": ["-I/usr/include/bpf/uapi"],
}


@subpackage("pahole-devel")
def _(self):
    return self.default_devel()
