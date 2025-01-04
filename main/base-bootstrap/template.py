pkgname = "base-bootstrap"
pkgver = "0.1"
pkgrel = 1
build_style = "meta"
depends = [
    "chimerautils",
    "apk-tools",
]
pkgdesc = "Minimal set of packages suitable for containers"
maintainer = "q66 <q66@chimera-linux.org>"
license = "custom:meta"
url = "https://chimera-linux.org"


match self.profile().arch:
    case "aarch64" | "ppc" | "ppc64" | "ppc64le" | "riscv64" | "x86_64":
        depends += ["chimera-repo-main"]
