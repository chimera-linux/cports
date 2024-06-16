pkgname = "pahole"
pkgver = "1.27"
_realver = "1.26"
pkgrel = 2
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
    "zlib-devel",
]
pkgdesc = "Debug information utilities"
maintainer = "q66 <q66@chimera-linux.org>"
license = "GPL-2.0-only"
url = "https://git.kernel.org/pub/scm/devel/pahole/pahole.git"
source = f"https://fedorapeople.org/~acme/dwarves/dwarves-{_realver}.tar.xz"
sha256 = "ad4c08339850e404609e2808012580b7e98366d2b91054bb93fe6dca94651fb4"
tool_flags = {
    # see libbpf comment about bpf headers
    "CFLAGS": ["-I/usr/include/bpf/uapi"],
    "CXXFLAGS": ["-I/usr/include/bpf/uapi"],
}
# no tests
options = ["!check"]


@subpackage("pahole-devel")
def _devel(self):
    return self.default_devel()
