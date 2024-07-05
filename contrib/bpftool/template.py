pkgname = "bpftool"
pkgver = "6.9.8"
pkgrel = 0
build_wrksrc = "tools/bpf/bpftool"
build_style = "makefile"
make_cmd = "gmake"
make_build_args = [
    "LLVM=1",
    "STRIP=/bin/true",
    "V=1",
    "libdir=/usr/lib",
    "mandir=/usr/share/man",
    "prefix=/usr",
    "sbindir=/usr/bin",
]
make_install_args = list(make_build_args)
make_use_env = True
hostmakedepends = [
    "gmake",
    "python",
]
makedepends = [
    "elfutils-devel",
    "libcap-devel",
    "linux-headers",
]
pkgdesc = "Linux kernel bpf manipulation tool"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://perf.wiki.kernel.org/index.php/Main_Page"
source = f"https://cdn.kernel.org/pub/linux/kernel/v{pkgver[:pkgver.find('.')]}.x/linux-{pkgver}.tar.xz"
sha256 = "f048267b7b88316c9ca708c68d15a9ae802dcfc943c3188c1273eb958c433281"
# nope
options = ["!check"]
