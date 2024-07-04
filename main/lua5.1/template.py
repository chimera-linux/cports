pkgname = "lua5.1"
pkgver = "5.1.5"
pkgrel = 0
build_style = "makefile"
make_build_target = "linux"
make_use_env = True
hostmakedepends = ["pkgconf"]
makedepends = ["libedit-readline-devel"]
pkgdesc = "Lua scripting language 5.1.x"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "https://lua.org"
source = f"https://www.lua.org/ftp/lua-{pkgver}.tar.gz"
sha256 = "2640fc56a795f29d28ef15e13c34a47e223960b0240e8cb0a82d9b0738695333"
tool_flags = {"CFLAGS": ["-fPIC", "-DLUA_USE_LINUX"]}
# TODO: contrib/lua5.1-lgi test crash
hardening = ["!int"]
# no test suite
options = ["!check"]

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

    self.rename(self.destdir / "usr/share/man/man1/lua.1", f"lua{_lver}.1")
    self.rename("usr/share/man/man1/luac.1", f"luac{_lver}.1")

    _libf = f"liblua{_lver}.so.{pkgver}"
    self.install_link(f"usr/lib/liblua{_lver}.so", _libf)
    self.install_link(f"usr/lib/liblua{_lver}.so.{_lver}", _libf)


@subpackage("lua5.1-devel")
def _devel(self):
    return self.default_devel()
