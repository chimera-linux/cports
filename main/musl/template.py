# keep in sync with musl-static-nolto
pkgname = "musl"
pkgver = "1.2.2"
pkgrel = 0
build_style = "gnu_configure"
configure_args = ["--prefix=/usr", "--disable-gcc-wrapper"]
make_cmd = "gmake"
hostmakedepends = ["gmake"]
provides = ["so:libc.so=0"]
pkgdesc = "Musl C library"
maintainer = "q66 <q66@chimera-linux.org>"
license = "MIT"
url = "http://www.musl-libc.org"
source = f"http://www.musl-libc.org/releases/{pkgname}-{pkgver}.tar.gz"
sha256 = "9b969322012d796dc23dda27a35866034fa67d8fb67e0e2c45c913c3d43219dd"
# segfaults otherwise
hardening = ["!scp"]
# does not ship tests + allow "broken" symlinks to true
options = ["bootstrap", "!check", "brokenlinks", "lto"]

def init_configure(self):
    # ensure that even early musl uses compiler-rt
    if self.stage == 0:
        self.env["LIBCC_LDFLAGS"] = "--rtlib=compiler-rt"
        return

def post_build(self):
    from cbuild.util import compiler

    self.cp(self.files_path / "getent.c", ".")
    self.cp(self.files_path / "getent.c", ".")
    self.cp(self.files_path / "getconf.c", ".")
    self.cp(self.files_path / "iconv.c", ".")

    cc = compiler.C(self)
    cc.invoke(["getent.c"], "getent")
    cc.invoke(["getconf.c"], "getconf")
    cc.invoke(["iconv.c"], "iconv")

def do_install(self):
    self.install_dir("usr/lib")
    # ensure all files go in /usr/lib
    self.install_link("usr/lib", "lib")

    self.make.install()

    # no need for the symlink anymore
    self.rm(self.destdir / "lib")

    self.install_dir("usr/bin")
    self.install_link("../lib/libc.so", "usr/bin/ldd")

    self.install_bin("iconv")
    self.install_bin("getent")
    self.install_bin("getconf")

    self.install_man(self.files_path / "getent.1")
    self.install_man(self.files_path / "getconf.1")

    self.install_link("true", "usr/bin/ldconfig")

@subpackage("musl-static")
def _static(self):
    self.pkgdesc = f"{pkgdesc} (static with LTO)"
    # prefer over musl-static-nolto
    self.provider_priority = 10

    return ["usr/lib/libc.a"]

@subpackage("musl-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    # the .a files are empty archives
    return ["usr/include", "usr/lib/*.o", "usr/lib/*.a"]
