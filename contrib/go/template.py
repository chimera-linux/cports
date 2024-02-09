pkgname = "go"
pkgver = "1.21.7"
pkgrel = 0
hostmakedepends = ["bash"]
checkdepends = [
    "libunwind-devel-static",
    "musl-devel-static",
    "libatomic-chimera-devel-static",
]
pkgdesc = "Go programming language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://go.dev"
source = f"{url}/dl/go{pkgver}.src.tar.gz"
sha256 = "00197ab20f33813832bff62fd93cca1c42a08cc689a32a6672ca49591959bff6"
env = {}
# a bunch of tests fail for now, so FIXME
options = [
    "!strip",
    "!debug",
    "!lto",
    "!check",
    "!scanrundeps",
    "!lintstatic",
    "foreignelf",
    "execstack",
]

# bootstrapping mode generates tarballs for go-bootstrap
# do not use a temporary directory mode when running this!
_bootstrap = False

if _bootstrap:
    options += ["!check"]
    env["GOROOT_FINAL"] = "/usr/lib/go-bootstrap"
else:
    env["GOROOT_FINAL"] = "/usr/lib/go"

if self.profile().cross:
    hostmakedepends += ["go"]
    env["GOROOT_BOOTSTRAP"] = "/usr/lib/go"
else:
    hostmakedepends += ["go-bootstrap"]
    env["GOROOT_BOOTSTRAP"] = "/usr/lib/go-bootstrap"

if self.profile().goarch:
    env["GOARCH"] = self.profile().goarch
else:
    broken = f"Unsupported platform ({self.profile().arch})"


def post_extract(self):
    # https://github.com/golang/go/issues/39905
    self.rm("src/cmd/link/internal/ld/fallocate_test.go")


def do_build(self):
    self.do(
        "bash",
        "make.bash",
        "-v",
        wrksrc="src",
        env={
            "GOROOT": str(self.chroot_cwd),
            "CC": "clang",
        },
    )


def do_check(self):
    self.do(self.chroot_cwd / "bin/go", "tool", "dist", "test", "-v", "-run")


def do_install(self):
    _binpath = "bin"
    if self.profile().cross:
        _binpath = f"bin/linux_{self.profile().goarch}"
        with self.profile("host") as hpf:
            _hostarch = hpf.goarch
    else:
        _hostarch = None

    def _clear_pkg(ppath):
        if _hostarch:
            self.rm(ppath / f"tool/linux_{_hostarch}", recursive=True)
            self.rm(ppath / f"linux_{_hostarch}", recursive=True)
        for f in (ppath / "tool").iterdir():
            self.rm(f / "api", force=True)

    if _bootstrap:
        bdirn = f"go-bootstrap-{pkgver}-{self.profile().goarch}"
        self.mkdir(bdirn)
        self.cp(_binpath, f"{bdirn}/bin", recursive=True)
        self.cp("src", bdirn, recursive=True)
        self.cp("pkg", bdirn, recursive=True)
        self.cp("LICENSE", bdirn)
        _clear_pkg(self.cwd / bdirn / "pkg")
        self.do("tar", "cvJf", f"{bdirn}.tar.xz", bdirn)
        self.rm(bdirn, recursive=True)
        self.error("build done, collect your tarball in builddir")

    self.install_files(_binpath, "usr/lib/go", name="bin")
    self.install_files("lib", "usr/lib/go")
    self.install_files("pkg", "usr/lib/go")
    self.install_files("src", "usr/lib/go")
    self.install_files("doc", "usr/lib/go")
    self.install_files("misc", "usr/lib/go")
    self.install_file("go.env", "usr/lib/go")
    self.install_file("VERSION", "usr/lib/go")

    self.install_dir("usr/bin")

    for f in (self.destdir / "usr/lib/go/bin").iterdir():
        self.install_link(f"../lib/go/bin/{f.name}", f"usr/bin/{f.name}")

    self.install_dir("usr/share/go")
    self.install_link("../../lib/go/doc", "usr/share/go/doc")
    self.install_link("../../lib/go/misc", "usr/share/go/misc")

    self.install_license("LICENSE")

    _clear_pkg(self.destdir / "usr/lib/go/pkg")
