pkgname = "zstd"
pkgver = "1.6.0"
pkgrel = 0
hostmakedepends = ["pkgconf"]
makedepends = ["lz4-devel", "xz-devel", "zlib-ng-compat-devel"]
checkdepends = ["file"]
renames = ["libzstd"]
pkgdesc = "Zstd compression utilities"
license = "BSD-3-Clause"
url = "http://www.zstd.net"
source = f"https://github.com/meta/zstd/releases/download/v{pkgver}/zstd-{pkgver}.tar.gz"
sha256 = "2ba599ae2a257976278e7e71e998433a387bfd18aa7b78678229fd5d84f5e9b8"
compression = "deflate"
hardening = ["!vis", "!cfi"]
# testing does a completely separate build of zstd which defeats the purpose
# also, replaces zstd program that is then installed with a different, static one
options = ["!check"]


def build(self):
    self.do("make", f"-j{self.make_jobs}", "PREFIX=/usr", "lib-mt")
    self.do(
        "make",
        f"-j{self.make_jobs}",
        "PREFIX=/usr",
        "-C",
        "programs",
        "zstd-dll",
        "LIB_BINDIR=../lib",
    )
    self.do("make", f"-j{self.make_jobs}", "PREFIX=/usr", "-C", "contrib/pzstd")


def check(self):
    self.do("make", "check")


def install(self):
    self.do("make", "PREFIX=/usr", f"DESTDIR={self.chroot_destdir}", "install")
    self.do(
        "make",
        "-C",
        "contrib/pzstd",
        "PREFIX=/usr",
        f"DESTDIR={self.chroot_destdir}",
        "install",
    )
    self.install_license("LICENSE")
    for tool in ["zstdgrep", "zstdless"]:
        self.uninstall(f"usr/bin/{tool}")
        self.uninstall(f"usr/share/man/man1/{tool}.1")


@split("progs")
def _(self):
    self.install_if = [self.parent]

    return self.default_progs()


@split("devel")
def _(self):
    self.provides = [self.with_pkgver("libzstd-devel")]

    return self.default_devel()
