pkgname = "bpftool"
pkgver = "7.7.0"
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
    "https://github.com/libbpf/libbpf/archive/f5dcbae736e5d7f83a35718e01be1a8e3010fa39.tar.gz",
]
source_paths = [".", "libbpf"]
sha256 = [
    "6d9937fa9cff83b0e7a1f64d4348819e36e34de1bfb9d2ba7c5b36d150431463",
    "2897bbd6df85be269fb4b0ccd3b7047f13ed8d400a27e58151192b152965a061",
]
# nope
options = ["!check"]
