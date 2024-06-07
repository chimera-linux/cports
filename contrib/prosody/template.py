pkgname = "prosody"
pkgver = "0.12.4"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_check_target = "test"
make_use_env = True
hostmakedepends = ["gmake"]
makedepends = [
    "icu-devel",
    "libidn2-devel",
    "linux-headers",
    "lua5.4-devel",
    "openssl-devel",
]
depends = [
    "lua5.4",
    "lua5.4-luaexpat",
    "lua5.4-luafilesystem",
    "lua5.4-luasec",
    "lua5.4-luasocket",
    "lua5.4-luaunbound",
]
checkdepends = depends + ["lua5.4-busted"]
pkgdesc = "Modern xmpp communication server"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://prosody.im"
source = f"https://prosody.im/downloads/source/prosody-{pkgver}.tar.gz"
sha256 = "47d712273c2f29558c412f6cdaec073260bbc26b7dda243db580330183d65856"


def do_configure(self):
    self.do(
        "./configure",
        f"--c-compiler={self.get_tool('CC')}",
        f"--linker={self.get_tool('CC')}",
        f"--add-cflags={self.get_cflags(shell=True)}",
        f"--ldflags={self.get_ldflags(shell=True)} -shared",
        "--prefix=/usr",
        "--libdir=/usr/lib",
        "--sysconfdir=/etc/prosody",
        "--ostype=linux",
        "--with-random=getrandom",
        "--with-lua-include=/usr/include",
        "--with-lua-lib=/usr/lib/lua/5.4",
        "--no-example-certs",
    )


def post_install(self):
    self.install_license("COPYING")
    self.install_sysusers(self.files_path / "sysusers.conf")
    self.install_tmpfiles(self.files_path / "tmpfiles.conf")
    self.install_service(self.files_path / "prosody")
