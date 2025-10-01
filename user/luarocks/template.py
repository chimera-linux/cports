pkgname = "luarocks"
pkgver = "3.13.0"
pkgrel = 0
build_style = "configure"
configure_args = [
    "--prefix=/usr",
    "--sysconfdir=/etc",
    "--lua-version=5.5",
    "--with-lua-include=/usr/include/lua5.5",
    "--rocks-tree=/usr/lib/luarocks",
]
hostmakedepends = ["curl", "lua5.5", "unzip"]
makedepends = ["lua5.5-devel"]
depends = ["curl", "lua5.5", "unzip"]
pkgdesc = "Package manager for Lua modules"
license = "MIT"
url = "https://luarocks.org"
source = f"{url}/releases/luarocks-{pkgver}.tar.gz"
sha256 = "245bf6ec560c042cb8948e3d661189292587c5949104677f1eecddc54dbe7e37"
# no tests
options = ["!check"]

_luavers = ["5.1", "5.2", "5.3", "5.4", "5.5"]


def post_build(self):
    for lv in _luavers[:-1]:
        self.do(
            "make",
            f"LUA_VERSION={lv}",
            f"LUA_INTERPRETER=lua{lv}",
            f"LUA_INCDIR=/usr/include/lua{lv}",
            f"./build/config-{lv}.lua",
        )


def post_install(self):
    self.install_license("COPYING")

    for lv in _luavers[:-1]:
        self.do(
            "make",
            f"LUA_VERSION={lv}",
            f"DESTDIR={self.chroot_destdir}",
            "install-config",
        )

    for lv in _luavers:
        fn = self.destdir / f"usr/bin/luarocks-{lv}"
        with fn.open("w") as outf:
            outf.write("#!/bin/sh\n")
            outf.write(f'exec /usr/bin/luarocks --lua-version {lv} "$@"')
        self.chmod(fn, 0o755)

        fn = self.destdir / f"usr/bin/luarocks-admin-{lv}"
        with fn.open("w") as outf:
            outf.write("#!/bin/sh\n")
            outf.write(f'exec /usr/bin/luarocks-admin --lua-version {lv} "$@"')
        self.chmod(fn, 0o755)


def _subpkg(lv):
    @subpackage(f"luarocks-lua{lv}")
    def _(self):
        self.subdesc = f"Lua {lv} support"
        self.options = ["etcfiles"]
        self.install_if = [self.parent, f"lua{lv}"]

        return [f"usr/bin/*-{lv}", f"etc/luarocks/config-{lv}.lua"]


for _lv in _luavers:
    _subpkg(_lv)
