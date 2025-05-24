pkgname = "pnpm"
pkgver = "10.11.0"
pkgrel = 0
hostmakedepends = ["nodejs"]
depends = ["nodejs"]
pkgdesc = "Package manager for Node"
license = "BSD-2-Clause"
url = "https://pnpm.io"
source = f"https://registry.npmjs.org/pnpm/-/pnpm-{pkgver}.tgz"
sha256 = "a69e9cb077da419d47d18f1dd52e207245b29cac6e076acedbeb8be3b1a67bd7"


def install(self):
    self.install_file(
        "dist/node_modules/v8-compile-cache/v8-compile-cache.js",
        "usr/lib/pnpm",
    )
    self.install_file("dist/pnpm.cjs", "usr/lib/pnpm")
    self.install_file("dist/worker.js", "usr/lib/pnpm")
    self.install_bin("bin/pnpm.cjs", name="pnpm")
    self.install_bin("bin/pnpx.cjs", name="pnpx")
    self.install_license("LICENSE")
