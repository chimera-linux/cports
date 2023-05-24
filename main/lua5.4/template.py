pkgname = "lua5.4"
pkgver = "5.4.4"
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
sha256 = "164c7849653b80ae67bec4b7473b884bf5cc8d2dca05653475ec2ed27b9ebf61"
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

    self.mv(
        self.destdir / "usr/share/man/man1/lua.1",
        self.destdir / f"usr/share/man/man1/lua{_lver}.1",
    )
    self.mv(
        self.destdir / "usr/share/man/man1/luac.1",
        self.destdir / f"usr/share/man/man1/luac{_lver}.1",
    )

    self.install_link(f"lua{_lver}.1", "usr/share/man/man1/lua.1")
    self.install_link(f"luac{_lver}.1", "usr/share/man/man1/luac.1")

    _libf = f"liblua{_lver}.so.{pkgver}"
    self.install_link(_libf, f"usr/lib/liblua{_lver}.so")
    self.install_link(_libf, f"usr/lib/liblua{_lver}.so.{_lver}")

    # this is the primary lua
    self.install_link(f"lua{_lver}", "usr/bin/lua")
    self.install_link(f"luac{_lver}", "usr/bin/luac")
    self.install_link(f"lua{_lver}.pc", "usr/lib/pkgconfig/lua.pc")


@subpackage("lua5.4-devel")
def _devel(self):
    return self.default_devel()
