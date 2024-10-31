pkgname = "bpftool"
pkgver = "7.5.0"
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
    "https://github.com/libbpf/libbpf/archive/09b9e83102eb8ab9e540d36b4559c55f3bcdb95d.tar.gz",
]
source_paths = [".", "libbpf"]
sha256 = [
    "a126f8cb06f887741ce45cd4f823583ae70aebc3f615cc4ed2a5eec8676a9681",
    "f94a66ab80e79aa11e15409479d8bc2572649f0ef25dbd2daf503ea5b05067ad",
]
# nope
options = ["!check"]
