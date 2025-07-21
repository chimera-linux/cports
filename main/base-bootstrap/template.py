pkgname = "base-bootstrap"
pkgver = "0.1"
pkgrel = 2
build_style = "meta"
depends = [
    "apk-tools",
    "chimerautils",
]
pkgdesc = "Minimal set of packages suitable for containers"
license = "custom:meta"
url = "https://chimera-linux.org"


match self.profile().arch:
    case (
        "aarch64"
        | "loongarch64"
        | "ppc"
        | "ppc64"
        | "ppc64le"
        | "riscv64"
        | "x86_64"
    ):
        depends += ["chimera-repo-main"]
