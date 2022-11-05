pkgname = "musl"
pkgver = "1.2.3"
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
sha256 = "7d5b0b6062521e4627e099e4c9dc8248d32a30285e959b7eecaa780cf8cfd4a4"
# segfaults otherwise
hardening = ["!scp"]
# does not ship tests + allow "broken" symlinks to true
options = ["bootstrap", "!check", "!lto", "brokenlinks"]

# without this, we will get two RW LOAD segments with p_filesz < p_memsz
# at least on ppc64 where .plt is SHT_NOBITS and therefore does not occupy
# any file space, while being inserted in the first RW LOAD segment
#
# this creates an issue as the linux kernel's interpreter code path does
# not handle this scenario (it ignores memsz, uses only filesz, and then
# adds a single bss mapping)
#
# this only the libc (interpreter) so apply the workaround here
match self.profile().arch:
    case "ppc64le" | "ppc64":
        tool_flags = {
            "LDFLAGS": ["-Wl,-z,lazy"]
        }

if self.stage > 0:
    # have base-files extract first in normal installations
    #
    # don't do this for stage 0 though, because otherwise base-files will
    # get installed as a makedepend and subsequently removed as an autodep,
    # which will nuke the base symlinks handled by initial initdb, as the
    # stage0 bldroot is not a complete chroot and relies on the external
    # state we give it during first setup
    #
    # but this only really matters for "real" systems, so in stage 0 we can
    # just avoid the dependency and work around the whole issue
    #
    depends = ["base-files"]

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

@subpackage("musl-devel-static")
def _static(self):
    return ["usr/lib/libc.a"]

@subpackage("musl-devel")
def _devel(self):
    self.depends = [f"{pkgname}={pkgver}-r{pkgrel}"]
    self.options = ["!splitstatic"]
    # the .a files are empty archives
    return ["usr/include", "usr/lib/*.o", "usr/lib/*.a"]
