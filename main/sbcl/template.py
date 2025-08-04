pkgname = "sbcl"
pkgver = "2.5.7"
pkgrel = 0
# riscv64 FIXME, ppc FIXME (dumps core during build)
archs = ["aarch64", "ppc64le", "x86_64"]
configure_args = [
    "--prefix=/usr",
    "--with-sb-core-compression",
    "--with-sb-dynamic-core",
    "--with-sb-test",
    "--with-sb-unicode",
]
hostmakedepends = [
    "ecl",
    "ecl-devel",
    "gc-devel",
    "gmp-devel",
    "libatomic_ops-devel",
    "libffi8-devel",
    "linux-headers",
    "texinfo",
]
makedepends = ["zstd-devel"]
checkdepends = ["strace"]
pkgdesc = "Steel Bank Common Lisp"
license = "custom:sbcl AND LOOP"
url = "https://www.sbcl.org"
source = f"$(SOURCEFORGE_SITE)/sbcl/sbcl-{pkgver}-source.tar.bz2"
sha256 = "c4fafeb795699d5bcff9085091acc762dcf5e55f85235625f3d7aef12c89d1d3"
# notably not pie on ppc64le due to asm stuff
nopie_files = ["usr/bin/sbcl"]
# tests are unreliable
options = ["!cross", "!lto", "!check"]


def init_configure(self):
    # only available on a few archs
    # --fancy implies threads
    match self.profile().arch:
        case "aarch64" | "riscv64" | "x86_64":
            self.configure_args += ["--fancy", "--with-sb-thread"]
    # build system ignores ldflags
    self.env["LINKFLAGS"] = str(self.get_ldflags(shell=True))
    # does not work on riscv64?
    if self.profile().arch != "riscv64":
        self.configure_args += ["--with-sb-linkable-runtime"]


def build(self):
    self.do("sh", "make.sh", "ecl", *self.configure_args)
    self.do("make", "info", wrksrc="doc/manual")


def check(self):
    self.do("sh", "run-tests.sh", wrksrc="tests")


def install(self):
    # on ppc64le it installs this and fails because missing dir? why
    self.install_dir("usr/tlsf-bsd/tlsf")
    self.do(
        "sh",
        "install.sh",
        env={"INSTALL_ROOT": str(self.chroot_destdir / "usr")},
    )
    # nuke that afterwards
    self.uninstall("usr/tlsf-bsd")

    self.install_license("COPYING")
    self.uninstall("usr/share/doc/sbcl/COPYING")
