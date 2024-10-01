pkgname = "sbcl"
pkgver = "2.4.9"
pkgrel = 0
# riscv64 FIXME
archs = ["aarch64", "ppc", "ppc64le", "x86_64"]
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
    "libffi-devel",
    "linux-headers",
    "texinfo",
]
makedepends = ["zstd-devel"]
checkdepends = ["strace"]
pkgdesc = "Steel Bank Common Lisp"
maintainer = "Paul A. Patience <paul@apatience.com>"
license = "custom:sbcl AND LOOP"
url = "https://www.sbcl.org"
source = f"$(SOURCEFORGE_SITE)/sbcl/sbcl-{pkgver}-source.tar.bz2"
sha256 = "9970e4ebc5d6943dc64d7ca1f52d9b5cd9fc94cef94d233213d78ec75f3605e2"
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
