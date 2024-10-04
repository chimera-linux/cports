pkgname = "lua5.4"
pkgver = "5.4.7"
pkgrel = 0
build_style = "makefile"
make_build_target = "linux-readline"
make_check_target = "test"
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = ["libedit-readline-devel"]
pkgdesc = "Lua scripting language 5.4.x"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://lua.org"
source = f"https://www.lua.org/ftp/lua-{pkgver}.tar.gz"
sha256 = "9fbf5e28ef86c69858f6d3d34eccc32e911c1a28b4120ff3e84aaa70cfbf1e30"
tool_flags = {"CFLAGS": ["-fPIC"]}

_lver = pkgname.removeprefix("lua")


def init_configure(self):
    _bins = [
        f"lua{_lver}",
        f"luac{_lver}",
    ]
    # do not install the symlinks as BSD install(1) resolves those
    _libs = [
        f"liblua{_lver}.a",
        f"liblua{_lver}.so.{pkgver}",
    ]

    self.make_build_args += [
        "CC=" + self.get_tool("CC"),
        "AR=" + self.get_tool("AR"),
        "MYCFLAGS=" + self.get_cflags(shell=True),
        "MYLDFLAGS=" + self.get_ldflags(shell=True),
    ]
    self.make_install_args += [
        "INSTALL_TOP=" + str(self.chroot_destdir / "usr"),
        "TO_BIN=" + " ".join(_bins),
        "TO_LIB=" + " ".join(_libs),
        "INSTALL_INC=" + str(self.chroot_destdir / f"usr/include/lua{_lver}"),
        "INSTALL_MAN=" + str(self.chroot_destdir / "usr/share/man/man1"),
    ]


def post_install(self):
    self.install_file(self.files_path / f"lua{_lver}.pc", "usr/lib/pkgconfig")
    self.install_license("doc/readme.html")

    self.rename("usr/share/man/man1/lua.1", f"lua{_lver}.1")
    self.rename("usr/share/man/man1/luac.1", f"luac{_lver}.1")

    self.install_link("usr/share/man/man1/lua.1", f"lua{_lver}.1")
    self.install_link("usr/share/man/man1/luac.1", f"luac{_lver}.1")

    _libf = f"liblua{_lver}.so.{pkgver}"
    self.install_link(f"usr/lib/liblua{_lver}.so", _libf)
    self.install_link(f"usr/lib/liblua{_lver}.so.{_lver}", _libf)

    # this is the primary lua
    self.install_link("usr/bin/lua", f"lua{_lver}")
    self.install_link("usr/bin/luac", f"luac{_lver}")
    self.install_link("usr/lib/pkgconfig/lua.pc", f"lua{_lver}.pc")


@subpackage("lua5.4-devel")
def _(self):
    return self.default_devel()
