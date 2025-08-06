pkgname = "bpftool"
pkgver = "7.6.0"
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
license = "GPL-2.0-only"
url = "https://github.com/libbpf/bpftool"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    # bpftool uses libbpf internals
    "https://github.com/libbpf/libbpf/archive/58dd1f58b57294b2e59482245b29e46f1812b82d.tar.gz",
]
source_paths = [".", "libbpf"]
sha256 = [
    "66ffaadb3043b300ce94c08a10d9a5e41e5f0bc5d221d8d19a4518e35ae6448c",
    "9d8960f81a8e08d112ba3ad83d3c676ec4b2d6aaf6969781a16213e6a8f3d4ed",
]
# nope
options = ["!check"]
