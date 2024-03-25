pkgname = "xwayland-run"
pkgver = "0.0.3"
pkgrel = 1
build_style = "meson"
configure_args = ["-Dcompositor=weston"]
hostmakedepends = ["meson"]
depends = [
    "python",
    "weston",
    "xauth",
    "xwayland",
]
pkgdesc = "Utilities around xwayland for running headless applications"
maintainer = "psykose <alice@ayaya.dev>"
license = "GPL-2.0-or-later"
url = "https://gitlab.freedesktop.org/ofourdan/xwayland-run"
source = f"{url}/-/archive/{pkgver}/xwayland-run-{pkgver}.tar.gz"
sha256 = "66cb0441fc71fb04838845478aef822e0a39fc2d803248b1e93651f9c5e75f46"
