pkgname = "prosody"
pkgver = "0.12.5"
pkgrel = 0
build_style = "makefile"
make_check_target = "test"
make_use_env = True
makedepends = [
    "icu-devel",
    "libidn2-devel",
    "linux-headers",
    "lua5.4-devel",
    "openssl3-devel",
]
depends = [
    "lua5.4",
    "lua5.4-luaexpat",
    "lua5.4-luafilesystem",
    "lua5.4-luasec",
    "lua5.4-luasocket",
    "lua5.4-luaunbound",
]
checkdepends = ["lua5.4-busted", *depends]
pkgdesc = "Modern xmpp communication server"
maintainer = "ttyyls <contact@behri.org>"
license = "MIT"
url = "https://prosody.im"
source = f"https://prosody.im/downloads/source/prosody-{pkgver}.tar.gz"
sha256 = "778fb7707a0f10399595ba7ab9c66dd2a2288c0ae3a7fe4ab78f97d462bd399f"


def configure(self):
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
