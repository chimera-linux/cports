pkgname = "bpftool"
pkgver = "6.8.9"
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
sha256 = "f905f1238ea7a8e85314bacf283302e8097006010d25fcea726d0de0ea5bc9b6"
# nope
options = ["!check"]
