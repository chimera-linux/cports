pkgname = "bpftool"
pkgver = "6.9"
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
sha256 = "24fa01fb989c7a3e28453f117799168713766e119c5381dac30115f18f268149"
# nope
options = ["!check"]
