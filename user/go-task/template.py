pkgname = "go-task"
pkgver = "3.45.4"
pkgrel = 2
build_style = "go"
make_build_args = [
    "./cmd/task",
]
hostmakedepends = ["go"]
pkgdesc = "Task runner / simpler Make alternative written in Go"
license = "MIT"
url = "https://taskfile.dev"
source = f"https://github.com/go-task/task/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "bca35c6d394be1c67422bb7aae9b1fc2cb83143a8a1d28f032388f1d926d3311"
# conditionally disabled check
options = []

# test suite expects amd64
if self.profile().arch != "x86_64":
    options += ["!check"]


def post_install(self):
    self.install_license("LICENSE")

    self.install_completion("completion/fish/task.fish", "fish", "task")
    self.install_completion("completion/bash/task.bash", "bash", "task")
    self.install_completion("completion/zsh/_task", "zsh", "task")
