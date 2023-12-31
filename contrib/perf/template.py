pkgname = "perf"
pkgver = "6.6.9"
pkgrel = 0
build_wrksrc = "tools/perf"
build_style = "makefile"
make_cmd = "gmake"
make_build_args = [
    "LLVM=1",
    "NO_LIBAUDIT=1",
    "NO_LIBBABELTRACE=1",
    "NO_LIBDEBUGINFOD=1",
    "NO_LIBPFM4=1",
    "NO_LIBTRACEEVENT=1",
    "NO_LIBUNWIND=1",
    "NO_SDT=1",
    "STRIP=/bin/true",
    "V=1",
    "libdir=/usr/lib",
    "mandir=/usr/share/man",
    "prefix=/usr",
    "sbindir=/usr/bin",
]
make_install_args = list(make_build_args)
hostmakedepends = [
    "bash",
    "bison",
    "flex",
    "gmake",
    "python-setuptools",
]
makedepends = [
    "elfutils-devel",
    "libcap-devel",
    "libnuma-devel",
    "linux-headers",
    "openssl-devel",
    "python-devel",
    "slang-devel",
    "xz-devel",
    "zlib-devel",
    "zstd-devel",
]
pkgdesc = "Linux performance analyzer"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-only"
url = "https://perf.wiki.kernel.org/index.php/Main_Page"
source = f"https://cdn.kernel.org/pub/linux/kernel/v{pkgver[:pkgver.find('.')]}.x/linux-{pkgver}.tar.xz"
sha256 = "8ebc65af0cfc891ba63dce0546583da728434db0f5f6a54d979f25ec47f548b3"
# nope
options = ["!check"]
# MAKE is ignored in some places
exec_wrappers = [("/usr/bin/gmake", "make")]


def post_install(self):
    # relink hardlink
    self.rm(self.destdir / "usr/bin/trace")
    self.install_link("perf", "usr/bin/trace")
    # valid as both
    self.rm(self.destdir / "etc/bash_completion.d", recursive=True)
    self.install_completion("perf-completion.sh", "bash")
    self.install_completion("perf-completion.sh", "zsh")
    # pointless tests
    self.rm(self.destdir / "usr/libexec/perf-core/tests", recursive=True)
