pkgname = "ai.robots.txt"
pkgver = "1.44"
pkgrel = 0
pkgdesc = "List of AI agents and robots to block"
license = "MIT"
url = "https://github.com/ai-robots-txt/ai.robots.txt"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "67f14eef069e0fb261ce64215965b28331513512b94b2793bb09fd3e458a3b65"
# no tests
options = ["!check"]


def install(self):
    self.install_license("LICENSE")
    for f in [
        ".htaccess",
        "Caddyfile",
        "haproxy-block-ai-bots.txt",
        "nginx-block-ai-bots.conf",
        "robots.json",
        "robots.txt",
    ]:
        self.install_file(f, "usr/share/ai.robots.txt")
