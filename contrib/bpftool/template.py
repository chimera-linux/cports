pkgname = "bpftool"
pkgver = "7.4.0"
pkgrel = 0
build_wrksrc = "src"
build_style = "makefile"
make_build_args = [
    "LLVM=1",
    "STRIP=/bin/true",
    "V=1",
    "libdir=/usr/lib",
    "mandir=/usr/share/man",
    "prefix=/usr",
    "sbindir=/usr/bin",
]
make_install_args = [*make_build_args]
make_use_env = True
hostmakedepends = [
    "python",
]
makedepends = [
    "elfutils-devel",
    "libcap-devel",
    "linux-headers",
    "llvm-devel",
]
pkgdesc = "Linux kernel bpf manipulation tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://github.com/libbpf/bpftool"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    # bpftool uses libbpf internals
    "https://github.com/libbpf/libbpf/archive/20ea95b4505c477af3b6ff6ce9d19cee868ddc5d.tar.gz",
]
source_paths = [".", "libbpf"]
sha256 = [
    "131c6284799dd955af7f581c5362b8f0704ea3af7e5c4eac49b3b91a064b6ad4",
    "f0c10bb89af29533b27146c8ea3dd1fa89905a8933387be782ead09488820db6",
]
# nope
options = ["!check"]
