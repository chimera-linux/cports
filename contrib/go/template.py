pkgname = "go"
pkgver = "1.19.1"
pkgrel = 0
hostmakedepends = ["bash"]
checkdepends = ["iana-etc", "libunwind-devel-static", "musl-devel-static"]
pkgdesc = "Go programming language"
maintainer = "q66 <q66@chimera-linux.org>"
license = "BSD-3-Clause"
url = "https://go.dev"
source = f"{url}/dl/go{pkgver}.src.tar.gz"
sha256 = "27871baa490f3401414ad793fba49086f6c855b1c584385ed7771e1204c7e179"
env = {}
# a bunch of tests fail for now, so FIXME
options = [
    "!strip", "!debug", "!lto", "!check", "!scanrundeps",
    "!lintstatic", "foreignelf",
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

match self.profile().arch:
    case "aarch64":
        env["GOARCH"] = "arm64"
    case "x86_64":
        env["GOARCH"] = "amd64"
    case "ppc64le" | "riscv64":
        env["GOARCH"] = self.profile().arch
    case _:
        broken = f"Unsupported platform ({self.profile().arch})"

def post_extract(self):
    # https://github.com/golang/go/issues/39905
    self.rm("src/cmd/link/internal/ld/fallocate_test.go")

def do_build(self):
    self.do(
        "bash", "make.bash", "-v", wrksrc = "src", env = {
            "GOROOT": str(self.chroot_cwd),
            "CC": "clang",
        }
    )

def do_check(self):
    self.do(self.chroot_cwd / "bin/go", "tool", "dist", "test", "-v", "-run")

def do_install(self):
    self.install_license("LICENSE")

    _binpath = "bin"
    if self.profile().cross:
        _binpath = f"bin/linux_{env['GOARCH']}"

    def _clear_pkg(ppath):
        self.rm(ppath / "obj", recursive = True)
        for f in (ppath / "tool").iterdir():
            self.rm(f / "api", force = True)
            if f.name.startswith("linux_"):
                if f.name == f"linux_{env['GOARCH']}":
                    continue
                self.rm(f, recursive = True)
        for f in ppath.glob("linux_*"):
            if f.name == f"linux_{env['GOARCH']}":
                continue
            self.rm(f, recursive = True)

    if _bootstrap:
        bdirn = f"go-bootstrap-{pkgver}-{env['GOARCH']}"
        self.mkdir(bdirn)
        self.cp(_binpath, f"{bdirn}/bin", recursive = True)
        self.cp("src", bdirn, recursive = True)
        self.cp("pkg", bdirn, recursive = True)
        self.cp("LICENSE", bdirn)
        _clear_pkg(self.cwd / bdirn / "pkg")
        self.do("tar", "cvJf", f"{bdirn}.tar.xz", bdirn)
        self.rm(bdirn, recursive = True)
        self.error("build done, collect your tarball in builddir")

    self.install_dir("usr/bin")
    self.install_dir("usr/lib/go")
    self.install_dir("usr/share/go")

    for f in (self.cwd / _binpath).iterdir():
        self.install_bin(f)

    self.install_files("lib", "usr/lib/go")
    self.install_files("pkg", "usr/lib/go")
    self.install_files("src", "usr/lib/go")

    self.install_files("doc", "usr/share/go")
    self.install_files("misc", "usr/share/go")

    self.install_file("VERSION", "usr/lib/go")

    self.install_link("../../share/go/doc", "usr/lib/go/doc")
    self.install_link("../../share/go/misc", "usr/lib/go/misc")
    self.install_link("../../bin", "usr/lib/go/bin")

    _clear_pkg(self.destdir / "usr/lib/go/pkg")
