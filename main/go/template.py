pkgname = "go"
pkgver = "1.24.6"
pkgrel = 0
hostmakedepends = ["bash"]
checkdepends = [
    "libatomic-chimera-devel-static",
    "libunwind-devel-static",
    "musl-devel-static",
]
pkgdesc = "Go programming language"
license = "BSD-3-Clause"
url = "https://go.dev"
source = f"{url}/dl/go{pkgver}.src.tar.gz"
sha256 = "e1cb5582aab588668bc04c07de18688070f6b8c9b2aaf361f821e19bd47cfdbd"
env = {}
# see below
options = [
    "!strip",
    "!debug",
    "!lto",
    "!scanrundeps",
    "!lintstatic",
    "foreignelf",
    "execstack",
]

match self.profile().arch:
    case "aarch64" | "riscv64":
        # FIXME: these fail for unknown reasons currently
        options += ["!check"]
    case "loongarch64" | "ppc64le":
        # assume gcc / gnu as
        options += ["!check"]

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


def build(self):
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


def _get_binpath(self):
    _binpath = "bin"
    if self.profile().cross:
        _binpath = f"bin/linux_{self.profile().goarch}"
        with self.profile("host") as hpf:
            _hostarch = hpf.goarch
    else:
        _hostarch = None
    return _binpath, _hostarch


def _clear_pkg(self, arch, ppath):
    if arch:
        self.rm(ppath / f"pkg/tool/linux_{arch}", recursive=True)
        self.rm(ppath / f"pkg/linux_{arch}", force=True, recursive=True)
    for f in (ppath / "pkg/tool").iterdir():
        self.rm(f / "api", force=True)

    # cleanup useless testdata
    for f in (ppath / "src").rglob("testdata"):
        self.rm(f, recursive=True)
    for f in (ppath / "src").rglob("*_test.go"):
        self.rm(f)


@custom_target("bootstrap", "build")
def _(self):
    _binpath, _hostarch = _get_binpath(self)

    bdirn = f"go-bootstrap-{pkgver}-{self.profile().goarch}"
    self.mkdir(bdirn)
    self.cp(_binpath, f"{bdirn}/bin", recursive=True)
    self.cp("src", bdirn, recursive=True)
    self.cp("pkg", bdirn, recursive=True)
    self.cp("LICENSE", bdirn)
    _clear_pkg(self, _hostarch, self.cwd / bdirn)
    self.do(
        "tar",
        "cvf",
        f"{bdirn}.tar.zst",
        "--zstd",
        "--options",
        f"zstd:compression-level=19,zstd:threads={self.make_jobs}",
        bdirn,
    )
    self.rm(bdirn, recursive=True)


def check(self):
    self.do(
        "./run.bash",
        "-no-rebuild",
        env={
            "GO_TEST_TIMEOUT_SCALE": "5",
            # each shard spawns its own jobs too, so cap this to 1/4 of the
            # configured jobcount (but +1 so 1 ends up as 1)
            "GO_TEST_SHARDS": str(int(self.make_jobs / 4) + 1),
        },
        wrksrc="src",
    )


def install(self):
    _binpath, _hostarch = _get_binpath(self)

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
        self.install_link(f"usr/bin/{f.name}", f"../lib/go/bin/{f.name}")

    self.install_dir("usr/share/go")
    self.install_link("usr/share/go/doc", "../../lib/go/doc")
    self.install_link("usr/share/go/misc", "../../lib/go/misc")

    self.install_license("LICENSE")

    _clear_pkg(self, _hostarch, self.destdir / "usr/lib/go")
