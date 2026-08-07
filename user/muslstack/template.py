pkgname = "muslstack"
pkgver = "0.0.1"  # Since the code is 1 file, the author has no releases.
_commit = "d19cc5866abce3ca59dfc1666df7cc97097d0933"
pkgrel = 0
hostmakedepends = ["go"]
pkgdesc = (
    "Utility to check and modify PT_GNU_STACK segment size in ELF binaries"
)
license = "MIT"
url = "https://github.com/yaegashi/muslstack"
source = f"{url}/archive/{_commit}.tar.gz"
sha256 = "5922759e8b3816abebf6c668b84da56f88c41da7878b779082c3bf817a78dd24"


def build(self):
    if "debug" in self.options:
        self.do(
            "go",
            "build",
            "-gcflags=all=-N -l",
            "-o",
            "muslstack",
            "main.go",
            env={"CGO_ENABLED": "0"},
        )
    else:
        self.do(
            "go",
            "build",
            "-ldflags",
            "-s -w",
            "-o",
            "muslstack",
            "main.go",
            env={"CGO_ENABLED": "0"},
        )


def install(self):
    self.install_bin("muslstack")
    self.install_license("LICENSE")
