pkgname = "esbuild"
pkgver = "0.28.0"
pkgrel = 3
build_style = "go"
make_build_args = ["./cmd/esbuild"]
hostmakedepends = ["go", "nodejs"]
pkgdesc = "JavaScript and CSS bundler and minifier"
license = "MIT"
url = "https://esbuild.github.io"
source = f"https://github.com/evanw/esbuild/archive/v{pkgver}.tar.gz"
sha256 = "7aae83b197db3fd695e6f378d30fd6cbddeb93e4b1057b2c41d36ecb1dfebbc2"


def post_build(self):
    self.do(
        "node", "scripts/esbuild.js", "npm/esbuild/package.json", "--version"
    )
    self.do("node", "scripts/esbuild.js", "./build/esbuild", "--neutral")


def post_install(self):
    self.install_dir("usr/lib/node_modules/esbuild/bin")

    self.install_file(
        "npm/esbuild/package.json", "usr/lib/node_modules/esbuild"
    )
    self.install_files("npm/esbuild/lib", "usr/lib/node_modules/esbuild")

    self.install_link(
        "usr/lib/node_modules/esbuild/bin/esbuild", "../../../../bin/esbuild"
    )

    self.install_license("LICENSE.md")
