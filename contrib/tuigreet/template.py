pkgname = "tuigreet"
pkgver = "0.8.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo"]
makedepends = ["rust-std"]
depends = ["greetd"]
pkgdesc = "Console greeter for greetd"
maintainer = "natthias <natthias@proton.me>"
license = "GPL-3.0-or-later"
url = "https://github.com/apognu/tuigreet"
source = f"https://github.com/apognu/tuigreet/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "ed371ebe288a3e5782f01681c6c4ed4786b470184af286fa0e7b8898e47c154e"
