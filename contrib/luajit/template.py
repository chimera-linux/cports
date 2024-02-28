pkgname = "luajit"
# See: https://github.com/LuaJIT/LuaJIT/blob/0d313b243194a0b8d2399d8b549ca5a0ff234db5/Makefile#L16-L26
_ct = "1707061634"
pkgver = f"2.1.{_ct}"
pkgrel = 0
build_style = "makefile"
make_cmd = "gmake"
make_build_target = "amalg"
make_use_env = True
hostmakedepends = [
    "gmake",
    "pkgconf",
]
makedepends = [
    "lua5.1",
    "lua5.1-bitop",
]
pkgdesc = "LuaJIT is a just-in-time compiler for the Lua programming language"
maintainer = "yvvki <yvvki@duck.com>"
license = "MIT"
url = "https://luajit.org/luajit.html"
_commit = "0d313b243194a0b8d2399d8b549ca5a0ff234db5"
source = f"https://repo.or.cz/luajit-2.0.git/snapshot/{_commit}.tar.gz"
sha256 = "4b29f310d9e982f8bfa18f0dcd4d979a23666943e690714bef0750d56b2cd64b"
# no check target
options = ["!check"]

def init_configure(self):
    _cflags = self.get_cflags(shell=True)
    _ldflags = self.get_ldflags(shell=True)

    self.make_build_args += [
        "PREFIX=/usr",
        "BUILDMODE=dynamic",
        "CC=" + self.get_tool("CC"),
        "HOST_LUA=lua5.1",
        "HOST_CFLAGS=" + self.get_cflags(shell=True),
        "HOST_LDFLAGS=" + self.get_ldflags(shell=True),
        "TARGET_CFLAGS=" + _cflags,
        "TARGET_LDFLAGS=" + _ldflags,
    ]

def post_install(self):
    self.install_license("COPYRIGHT")
