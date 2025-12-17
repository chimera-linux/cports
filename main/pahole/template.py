pkgname = "pahole"
pkgver = "1.30"
pkgrel = 1
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
license = "GPL-2.0-only"
url = "https://git.kernel.org/pub/scm/devel/pahole/pahole.git"
source = f"https://fedorapeople.org/~acme/dwarves/dwarves-{pkgver}.tar.xz"
sha256 = "1c89f47dc4f127c4b9d3fb46c8386a40be45c36ef82e8df472418de9423fc5bb"
tool_flags = {
    # see libbpf comment about bpf headers
    "CFLAGS": ["-I/usr/include/bpf/uapi"],
    "CXXFLAGS": ["-I/usr/include/bpf/uapi"],
}


@subpackage("pahole-devel")
def _(self):
    return self.default_devel()
