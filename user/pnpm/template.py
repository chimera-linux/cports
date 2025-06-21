pkgname = "pnpm"
pkgver = "10.12.1"
pkgrel = 0
hostmakedepends = ["nodejs"]
depends = ["nodejs"]
pkgdesc = "Package manager for Node"
license = "BSD-2-Clause"
url = "https://pnpm.io"
source = f"https://registry.npmjs.org/pnpm/-/pnpm-{pkgver}.tgz"
sha256 = "889bac470ec93ccc3764488a19d6ba8f9c648ad5e50a9a6e4be3768a5de387a3"


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
