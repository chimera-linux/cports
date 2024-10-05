pkgname = "pass-otp"
pkgver = "1.2.0"
pkgrel = 1
build_style = "makefile"
make_install_args = ["BASHCOMPDIR=/usr/share/bash-completion/completions"]
depends = ["password-store", "oath-toolkit", "qrencode"]
pkgdesc = "Pass extension for managing one-time-password (OTP) tokens"
maintainer = "Jan Christian Grünhage <jan.christian@gruenhage.xyz>"
license = "GPL-3.0-or-later"
url = "https://github.com/tadfisher/pass-otp"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "5720a649267a240a4f7ba5a6445193481070049c1d08ba38b00d20fc551c3a67"
# Has no test suite
# Does not have a command to match the completion
options = ["!check", "!lintcomp"]
