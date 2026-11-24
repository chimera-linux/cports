pkgname = "bpftool"
pkgver = "7.8.1"
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
    "openssl3-devel",
]
pkgdesc = "Linux kernel bpf manipulation tool"
license = "GPL-2.0-only"
url = "https://github.com/libbpf/bpftool"
source = [
    f"{url}/archive/refs/tags/v{pkgver}.tar.gz",
    # bpftool uses libbpf internals
    "https://github.com/libbpf/libbpf/archive/85c0d575a447651bbeb8e2376eacd64c30dce9a6.tar.gz",
]
source_paths = [".", "libbpf"]
sha256 = [
    "71d06c175b51a4c8dd8ddebe859384d6a17cc8c57216e345395f5d48aa695c09",
    "6afe4301effebd56f976847603f86b30cca07d2ac8f954c95778463ec79d4d3f",
]
# nope
options = ["!check", "llvmflags"]
