pkgname = "prosody"
pkgver = "0.13.0"
_ver = "13.0.0"
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
license = "MIT"
url = "https://prosody.im"
source = f"https://prosody.im/downloads/source/prosody-{_ver}.tar.gz"
sha256 = "4309c5cfeb1a74d3f97185f6243a0c1068eb39fa7e91abc42cf2194bf067fc54"


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
