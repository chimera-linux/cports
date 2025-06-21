pkgname = "prosody"
pkgver = "13.0.2"
pkgrel = 1
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
    "luarocks5.4",
]
checkdepends = ["lua5.4-busted", *depends]
pkgdesc = "Modern xmpp communication server"
license = "MIT"
url = "https://prosody.im"
source = f"https://prosody.im/downloads/source/prosody-{pkgver}.tar.gz"
sha256 = "3e61bd396f37ca5245debfd6be49a47a6191332f0faa2d4ee5f00fbb040addb0"


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
