pkgname = "libbpf"
pkgver = "1.4.2"
pkgrel = 0
build_wrksrc = "src"
build_style = "makefile"
make_cmd = "gmake"
make_install_args = ["LIBSUBDIR=lib"]
hostmakedepends = [
    "gmake",
    "pkgconf",
]
makedepends = [
    "elfutils-devel",
    "linux-headers",
    "zlib-devel",
]
pkgdesc = "Linux BPF userspace library"
maintainer = "psykose <alice@ayaya.dev>"
license = "LGPL-2.1-only OR BSD-2-Clause"
url = "https://github.com/libbpf/libbpf"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "cfa2b6fbafab9608a2ab90d0eaf64f05c27dbf76d81bed516385e825f1aad502"
# FIXME: cfi
hardening = ["vis", "!cfi"]
# no tests
options = ["!check"]


def post_install(self):
    self.install_license("../LICENSE.BSD-2-Clause")
    # these headers are the 'latest' bpf headers, newer than what linux-headers
    # provides.
    # libbpf headers require using these latest bpf headers (that come from the
    # libbpf bpf-next tree) instead of the released (linux-headers stable) ones,
    # so place them in a separate private dir to use with -I later
    # https://gitlab.alpinelinux.org/alpine/aports/-/issues/13338
    with self.pushd("../include/uapi/linux"):
        self.install_file("bpf.h", "usr/include/bpf/uapi/linux")
        self.install_file("bpf_common.h", "usr/include/bpf/uapi/linux")
        self.install_file("btf.h", "usr/include/bpf/uapi/linux")


@subpackage("libbpf-devel")
def _devel(self):
    return self.default_devel()
