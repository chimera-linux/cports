pkgname = "redis"
pkgver = "7.2.4"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_args = ["BUILD_TLS=yes", "USE_JEMALLOC=no"]
hostmakedepends = ["gmake", "pkgconf"]
makedepends = ["openssl-devel"]
checkdepends = ["tcl", "procps"]
pkgdesc = "In-memory key-value datastore"
maintainer = "yanchan09 <yan@omg.lol>"
license = "BSD-3-Clause"
url = "https://redis.io"
source = f"https://github.com/{pkgname}/{pkgname}/archive/{pkgver}.tar.gz"
sha256 = "0a62b9ae89b4be4e8d40c0035c83a72cb6776f4b62fe53553981a57f0f4ff73d"
hardening = ["vis", "cfi"]


def do_install(self):
    self.make.install(
        [f"PREFIX={self.chroot_destdir / 'usr'}"], default_args=False
    )


def post_install(self):
    self.install_file(
        self.files_path / "sysusers.conf",
        "usr/lib/sysusers.d",
        name="redis.conf",
    )
    self.install_file(
        self.files_path / "tmpfiles.conf",
        "usr/lib/tmpfiles.d",
        name="redis.conf",
    )
    self.install_file(self.cwd / "redis.conf", "etc/redis")
    self.install_file(self.cwd / "sentinel.conf", "etc/redis")
    self.install_service(self.files_path / "redis")
    self.install_license("COPYING")
