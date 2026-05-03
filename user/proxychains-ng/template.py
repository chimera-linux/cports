pkgname = "proxychains-ng"
pkgver = "4.17"
pkgrel = 0
build_style = "gnu_configure"
configure_gen = []
make_dir = "."
pkgdesc = "Hook preloader to redirect TCP traffic through SOCKS or HTTP proxies"
license = "GPL-2.0-only"
url = "https://github.com/rofl0r/proxychains-ng"
source = f"{url}/releases/download/v{pkgver}/proxychains-ng-{pkgver}.tar.xz"
sha256 = "36ddc7f64cb3df2ca4170627c6e0f0dea33d1a6d0730629dff6f5c633f2006f9"
# Its tests need manually build and run
options = ["!check"]


def post_install(self):
    self.install_files("src/proxychains.conf", "usr/share/etc/")
    self.install_completion(
        "completions/zsh/_proxychains4", "zsh", name="proxychains4"
    )
